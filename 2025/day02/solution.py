PART_ONE_SAMPLE_ANSWER = 1227775554
PART_TWO_SAMPLE_ANSWER = 4174379265
SAMPLE_FILENAME = "sample.txt"
REAL_DATA_FILENAME = "data.txt"

import re

def compute_answer(filename: str, func, answer: int = None):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    
    res = func(lines)

    if answer is not None:
        print("sample answer is:", res)
        assert res == answer

    return res


def part_two_code(lines: list):
    data: list[str] = lines[0].split(',')

    count = 0

    for product in data:
        first, last = [int(x) for x in product.split('-')]

        for id in range(first, last + 1):

            string = str(id)
            matches = re.findall(r"^(\d+)\1+$", string)

            if matches:
                count += id

    return count


def part_one_code(lines: list):
    data: list[str] = lines[0].split(',')

    count = 0

    for product in data:
        first, last = [int(x) for x in product.split('-')]

        for id in range(first, last + 1):

            string = str(id)
            l = len(string)

            # print(string[:(l // 2)], string[(l // 2):])
            if string[:(l // 2)] == string[(l // 2):]:
                count += id

    return count


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

