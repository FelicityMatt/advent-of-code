PART_ONE_SAMPLE_ANSWER = 0
PART_TWO_SAMPLE_ANSWER = 0
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


def part_one_code(lines: list):
    pass


def part_two_code(lines: list):
    pass


if __name__ == '__main__':
    print('--------- part one ---------')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('--------- part two ---------')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part two answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('----------------------------')

