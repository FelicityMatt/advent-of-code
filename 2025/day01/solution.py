PART_ONE_SAMPLE_ANSWER = 3
PART_TWO_SAMPLE_ANSWER = 6
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
    cur = 50
    count = 0

    for line in lines:
        dir = line[0]
        num = int(line[1:])

        if dir == 'L':
            cur -= num % 100
            if cur < 0:
                cur += 100

        elif dir == 'R':
            cur += num % 100
            if cur >= 100:
                cur -= 100

        else:
            print("unknown:", dir)

        print(dir, num, cur)

        if cur == 0:
            count += 1

    return count


def part_two_code(lines: list):
    cur = 50
    count = 0

    for line in lines:
        dir = line[0]
        num = int(line[1:])
        prev = cur

        if dir == 'L':
            cur -= num % 100
            count += num // 100
            print(f"plus {num // 100}")
            if cur < 0:
                cur += 100
                if prev != 0:
                    count += 1
                    print("plus 1")

        elif dir == 'R':
            cur += num % 100
            count += num // 100
            print(f"plus {num // 100}")
            if cur > 100:
                cur -= 100
                count += 1
                print("plus 1")
            elif cur == 100:
                cur = 0

        else:
            print("unknown:", dir)

        print(dir, num, cur)

        if cur == 0:
            count += 1

    return count


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

