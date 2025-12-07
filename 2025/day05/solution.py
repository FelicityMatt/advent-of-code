PART_ONE_SAMPLE_ANSWER = 3
PART_TWO_SAMPLE_ANSWER = 14
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
    middle = lines.index("")
    ranges = lines[:middle]
    ranges = [[int(r) for r in line.split("-")] for line in ranges]

    fruits = list(map(int, lines[middle+1:]))
    fresh = 0

    for fruit in fruits:
        for r in ranges:
            if r[0] <= fruit <= r[1]:
                fresh += 1
                break

    return fresh

def part_two_code(lines: list):
    middle = lines.index("")
    ranges = lines[:middle]
    ranges = [[int(r) for r in line.split("-")] for line in ranges]

    changes = 1

    while changes > 0:
        result = []
        changes = 0

        for r in ranges:
            updated = False
            for e in result:
                # left is in existing range
                if e[0] <= r[0] <= e[1]:
                    e[0] = min(r[0], e[0])
                    e[1] = max(r[1], e[1])
                    updated = True
                # right is in existing range
                elif e[0] <= r[1] <= e[1]:
                    e[0] = min(r[0], e[0])
                    e[1] = max(r[1], e[1])
                    updated = True
                # new is outside existing range
                elif e[0] > r[0] and e[1] < r[1]:
                    e[0] = min(r[0], e[0])
                    e[1] = max(r[1], e[1])
                    updated = True

                if updated:
                    changes += 1

            if not updated:
                result.append(r)
        ranges = result

    fresh = 0
    for r in ranges:
        fresh += r[1] - r[0] + 1

    return fresh

if __name__ == '__main__':
    print('--------- part one ---------')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('--------- part two ---------')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part two answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('----------------------------')
