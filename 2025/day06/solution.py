PART_ONE_SAMPLE_ANSWER = 4277556
PART_TWO_SAMPLE_ANSWER = 3263827
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
    operators = [x.strip() for x in filter(lambda x: x != '', lines[-1].split(" "))]

    numbers = lines[:-1]
    numbers = [[int(x.strip()) for x in filter(lambda x: x != '', line.split(" "))] for line in numbers]

    total = 0

    for col in range(len(numbers[0])):
        nums = [row[col] for row in numbers]

        result = nums[0]
        for num in nums[1:]:
            if operators[col] == "+":
                result += num

            elif operators[col] == "*":
                result *= num

            else:
                print("UNKNOWN", operators[col])

        total += result

    return total

def part_two_code(lines: list):
    operators = [x.strip() for x in filter(lambda x: x != '', lines[-1].split(" "))]

    numbers = lines[:-1]
    numbers = [[x.strip() for x in filter(lambda x: x != '', line.split(" "))] for line in numbers]

    total = 0

    for col in range(len(numbers[0])):
        nums = [row[col] for row in numbers]

        width = max(len(s) for s in nums)
        padded = [s.zfill(width) for s in nums]
        # padded.reverse()
        print(padded)

        nums = ["".join([padded[r][c] for r in range(len(nums))]) for c in range(width)]
        print(nums)
        nums = [x.rstrip("0") for x in nums]
        nums = list(map(int, nums))
        print(nums)

        result = nums[0]
        for num in nums[1:]:
            if operators[col] == "+":
                result += num

            elif operators[col] == "*":
                result *= num

            else:
                print("UNKNOWN", operators[col])
        print(nums, result)
        total += result

    return total


if __name__ == '__main__':
    print('--------- part one ---------')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('--------- part two ---------')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part two answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('----------------------------')

