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
    cave = [list(map(int, line)) for line in lines]
    pointsDist = dict()
    # (row, column)
    currentPoints = [(0,0)]
    pointsDist[currentPoints[0]] = 0
    visitedPoints = []

    while len(currentPoints) != 0:
        newPoints = []
        # print('--- new iteration of current points ---')

        for currentPoint in currentPoints:
            currentDist = pointsDist[currentPoint]

            visitedPoints.append(currentPoint)
            row, col = currentPoint
            # all the neighbors' coordinates are found
            up = (row - 1, col) if row != 0 else 20
            down = (row + 1, col) if row != len(cave) - 1 else 20
            left = (row, col - 1) if col != 0 else 20
            right = (row, col + 1) if col != len(cave[0]) - 1 else 20

            neighbors = (up, down, left, right)

            # for each neighbor the distance from the current point to it is found and if that dist
            # is shorter than a previous found dist than it is set to that dist
            for neighbor in neighbors:
                if neighbor != 20:
                    newDist = currentDist + cave[neighbor[0]][neighbor[1]]
                    if neighbor not in pointsDist or pointsDist[neighbor] > newDist:
                        pointsDist[neighbor] = newDist
                        newPoints.append(neighbor)

        # each neighbor becomes a new point to be iterated through
        currentPoints = newPoints

    #returns the shortest distance to the bottom right point
    return pointsDist[(len(cave) - 1, len(cave[-1]) - 1)]


def part_one_code_recursion(lines: list):
    risks = []

    def cavedive(rowAndCol: tuple, currentPath: list, coordHistory: list):
        row, col = rowAndCol

        if sum(currentPath) > sampleMax:
            return None
        elif row == len(cave) - 1 and col == len(cave[0]) - 1:
            print('we reached the corner')
            print('current path is:', currentPath)
            risks.append(sum(currentPath[1:]) + cave[rowAndCol[0]][rowAndCol[1]])
        elif rowAndCol not in coordHistory:
            currentPath = currentPath[:]
            currentPath.append(cave[rowAndCol[0]][rowAndCol[1]])

            coordHistory = coordHistory[:]
            coordHistory.append(rowAndCol)

            up = (row - 1, col) if row != 0 else 20
            down = (row + 1, col) if row != len(cave) - 1 else 20
            left = (row, col - 1) if col != 0 else 20
            right = (row, col + 1) if col != len(cave[0]) - 1 else 20

            pointsList = (up, down, left, right)

            for point in pointsList:

                if point != 20 and point not in coordHistory:
                    cavedive(point, currentPath, coordHistory)

    cave = [list(map(int, line)) for line in lines]
    samplePath = [i[0] for i in cave] + cave[-1][1:]
    sampleMax = sum(samplePath)

    cavedive((0, 0), [], [])
    return min(risks)


def part_one_code1(lines: list):
    risk = 0
    x, y = [0, 0]
    print(len(lines))
    print(len(lines[0]))
    while (x, y) != (len(lines[0]) - 1, len(lines) - 1):
        right = int(lines[y][x + 1]) if x < (len(lines[0])) else 10
        left = int(lines[y + 1][x]) if y < (len(lines)) else 10
        if right < left:
            risk += right
            x += 1
        else:
            risk += left
            y += 1
        print((x, y))
    print(risk)
    return risk


def part_two_code(lines: list):
    initCave = [list(map(int, line)) for line in lines]
    rows = len(initCave)
    cols = len(initCave[0])
    caveSystem = [x[:] for x in initCave]

    def plusOne(cave):
        newCave = [x[:] for x in cave]
        for i in range(len(cave)):
            for j in range(len(cave[0])):
                newCave[i][j] += 1
                if newCave[i][j] == 10:
                    newCave[i][j] = 1
        return newCave


    # adding four caves down each time increasing all by one
    lastCave = initCave
    for _ in range(4):
        newCave = plusOne(lastCave)
        caveSystem += newCave
        lastCave = newCave

    for _ in range(4):
        for x in range(5):
            lastCave = [cave[-cols:] for cave in caveSystem[x*rows : (x+1)*rows]]
            newCave = plusOne(lastCave)
            for i in range(rows):
                caveSystem[x*rows + i] += newCave[i]

    return part_one_code(caveSystem)



if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 40)
    # do_it(True, 'day15_data.txt') #513 is not the answer
    print('----- part two -----')
    test(False, example, 315)
    do_it(False, 'day15_data.txt')
