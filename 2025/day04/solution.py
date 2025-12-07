PART_ONE_SAMPLE_ANSWER = 13
PART_TWO_SAMPLE_ANSWER = 43
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
    count = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lil_count = 0

            if lines[i][j] != '@':
                continue

            for dis_i in [-1, 0, 1]:
                for dis_j in [-1, 0, 1]:
                    new_i = i+dis_i
                    new_j = j+dis_j

                    if new_i == 0 and new_j == 0:
                        continue

                    if 0 > new_i or new_i >= len(lines):
                        continue

                    if 0 > new_j or new_j >= len(lines[0]):
                        continue

                    if lines[new_i][new_j] == '@':
                        lil_count += 1

            if lil_count <= 4:
                count += 1

    return count


def search_and_remove(lines: list):
    positions = []

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lil_count = 0

            if lines[i][j] != '@':
                continue

            for dis_i in [-1, 0, 1]:
                for dis_j in [-1, 0, 1]:
                    new_i = i+dis_i
                    new_j = j+dis_j

                    if new_i == 0 and new_j == 0:
                        continue

                    if 0 > new_i or new_i >= len(lines):
                        continue

                    if 0 > new_j or new_j >= len(lines[0]):
                        continue

                    if lines[new_i][new_j] == '@':
                        lil_count += 1

            if lil_count <= 4:
                positions.append((i,j))

    grid = [list(row) for row in lines]

    for i, j in positions:
        grid[i][j] = '.'

    # convert back to strings if needed
    new_lines = ["".join(row) for row in grid]

    return len(positions), new_lines
def part_two_code(lines: list):
    count = 0
    result = 1

    while result > 0:

        result, lines = search_and_remove(lines)
        count += result

    return count


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

