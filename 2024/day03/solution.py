PART_ONE_SAMPLE_ANSWER = 161
PART_TWO_SAMPLE_ANSWER = 48
SAMPLE_FILENAME = "sample.txt"
REAL_DATA_FILENAME = "data.txt"

def compute_answer(filename: str, func, answer: int = None):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    
    res = func(lines)

    if answer is not None:
        print("sample answer is:", res)
        assert res == answer

    return res



def get_next_mul(string: str):
    mutable_string = string[:]
    while "mul" in mutable_string:
        mutable_string = mutable_string[mutable_string.index("mul")+3:]
        yield mutable_string
        

MIN_DIGIT = 1
MAX_DIGIT = 3
MAX_LENGTH = MAX_DIGIT * 2 + 3

def part_one_code(lines: list):
    line = lines[0]

    total = 0
    for mul_suffix in get_next_mul(line):
        section = mul_suffix[:min(MAX_LENGTH, len(mul_suffix))]
        if '(' != section[0] or ')' not in section or ',' not in section:
            continue
        
        right_brac = section.index(')')

        numbers = section[1:right_brac].split(',')

        if len(numbers) != 2:
            continue
        
        if not all([x.isdigit() for x in numbers]):
            continue
        
        total += int(numbers[0]) * int(numbers[1])


    return total

def get_next_mul_with_context(string: str):
    mutable_string = string[:]
    enable = True
    while "mul" in mutable_string:
        do_index = float("inf")
        if "do()" in mutable_string:
            do_index = mutable_string.index('do()')

        dont_index = float("inf")
        if "don't()" in mutable_string:
            dont_index = mutable_string.index("don't()")
        
        next_mul_index = mutable_string.index("mul")
        if do_index < next_mul_index and do_index < dont_index:
            enable = True
        elif dont_index < next_mul_index and dont_index < do_index:
            enable = False

        mutable_string = mutable_string[next_mul_index+3:]
        yield mutable_string, enable

def part_two_code(lines: list):
    line = lines[0]

    total = 0
    for mul_suffix, enable in get_next_mul_with_context(line):
        if not enable:
            continue

        section = mul_suffix[:min(MAX_LENGTH, len(mul_suffix))]
        if '(' != section[0] or ')' not in section or ',' not in section:
            continue
        
        right_brac = section.index(')')

        numbers = section[1:right_brac].split(',')

        if len(numbers) != 2:
            continue
        
        if not all([x.isdigit() for x in numbers]):
            continue
        
        total += int(numbers[0]) * int(numbers[1])


    return total


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer("sample_2.txt", part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

