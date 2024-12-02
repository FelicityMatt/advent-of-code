def test(is_part_one: bool, example: list, answer: int):
    # test for part one
    if is_part_one:
        x = part_one_code(example)
        print('sample answer is:', x)
        assert x == answer
    # test for part two
    elif not is_part_one:
        x = part_two_code(example)
        print('sample answer is:', x)
        assert x == answer


def do_it(is_part_one, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        # for part one
        if is_part_one:
            x = part_one_code(lines)
            print('the answer to part one is:', x)
        # for part two
        elif not is_part_one:
            x = part_two_code(lines)
            print('the answer to part two is:', x)


def part_one_code(lines: list):
    # in a step:
    # 1. the energy of each octopus increases by 1

    # 2. an octopus Flashes if it has an energy level greater than 9
    #   causes increases in the octopi eight around it, which may cause them to flash too
    #   an octopus may only flash once per step

    # 3. an octopus that flashed is set to 0

    def flash(row,column):
        # start at top and end at top left
        rowInc = [1, 1, 0, -1, -1, -1, 0, 1]
        colInc = [0, 1, 1, 1, 0, -1, -1, -1]

        numFlashes = 1
        octopi[row][column] = 0
        for i in range(8):
            rowNum = row + rowInc[i] if 0 <= row + rowInc[i] <= 9 else None
            colNum = column + colInc[i] if 0 <= column + colInc[i] <= 9 else None
            if colNum is not None and rowNum is not None and octopi[rowNum][colNum] != 0:
                octopi[rowNum][colNum] += 1
                if octopi[rowNum][colNum] > 9:
                    numFlashes += flash(rowNum,colNum)
        return numFlashes

    octopi = []
    for line in lines:
        octopi.append([int(x) for x in line])

    totalFlashes = 0
    for _ in range(100):
        for i in range(len(octopi)):
            for j in range(len(octopi[0])):
                octopi[i][j] += 1

        for i in range(len(octopi)):
            for j in range(len(octopi[0])):
                if octopi[i][j] > 9:
                    totalFlashes += flash(i,j)

    return totalFlashes


def part_two_code(lines: list):
    def flash(row, column):
        # start at top and end at top left
        rowInc = [1, 1, 0, -1, -1, -1, 0, 1]
        colInc = [0, 1, 1, 1, 0, -1, -1, -1]

        numFlashes = 1
        octopi[row][column] = 0
        for i in range(8):
            rowNum = row + rowInc[i] if 0 <= row + rowInc[i] <= 9 else None
            colNum = column + colInc[i] if 0 <= column + colInc[i] <= 9 else None
            if colNum is not None and rowNum is not None and octopi[rowNum][colNum] != 0:
                octopi[rowNum][colNum] += 1
                if octopi[rowNum][colNum] > 9:
                    numFlashes += flash(rowNum, colNum)
        return numFlashes

    octopi = []
    for line in lines:
        octopi.append([int(x) for x in line])

    step = 0
    totalFlashes = 0

    while totalFlashes < 100:
        totalFlashes = 0
        for i in range(len(octopi)):
            for j in range(len(octopi[0])):
                octopi[i][j] += 1

        for i in range(len(octopi)):
            for j in range(len(octopi[0])):
                if octopi[i][j] > 9:
                    totalFlashes += flash(i, j)
        step += 1

    return step



if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 1656)
    do_it(True, 'day11_data.txt')
    print('----- part two -----')
    test(False, example, 195)
    do_it(False, 'day11_data.txt')
