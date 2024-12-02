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


def part_one_code(hightmap: list):
    def isLowPoint(row, column):
        point = int(hightmap[row][column])
        up = int(hightmap[row - 1][column]) if row != 0 else 10
        down = int(hightmap[row + 1][column]) if row != (len(hightmap) - 1) else 10
        left = int(hightmap[row][column - 1]) if column != 0 else 10
        right = int(hightmap[row][column + 1]) if column != len(hightmap[0]) - 1 else 10

        pointsList = (up,down,left,right)
        if min(point, up, down, left, right) == point and point not in pointsList:
            return True
        else:
            return False

    lowPoints = []
    for row in range(len(hightmap)):
        for column in range(len(hightmap[0])):
            if isLowPoint(row, column):
                lowPoints.append(int(hightmap[row][column]) + 1)

    return sum(lowPoints)



def part_two_code(hightmap: list):
    def isLowPoint(row, column):
        point = int(hightmap[row][column])
        up = int(hightmap[row - 1][column]) if row != 0 else 9
        down = int(hightmap[row + 1][column]) if row != (len(hightmap) - 1) else 9
        left = int(hightmap[row][column - 1]) if column != 0 else 9
        right = int(hightmap[row][column + 1]) if column != len(hightmap[0]) - 1 else 9

        pointsList = (up,down,left,right)
        if min(point, up, down, left, right) == point and point not in pointsList:
            return True
        else:
            return False

    def findBasinSize(rowAndColumn: tuple):
        if hightmap[rowAndColumn[0]][rowAndColumn[1]] == 9 or rowAndColumn in doneList:
            doneList.append(rowAndColumn)
            return 0
        else:
            up = (rowAndColumn[0] - 1, rowAndColumn[1]) if rowAndColumn[0] != 0 else None
            down = (rowAndColumn[0] + 1, rowAndColumn[1]) if rowAndColumn[0] != (len(hightmap) - 1) else None
            left = (rowAndColumn[0], rowAndColumn[1] - 1) if rowAndColumn[1] != 0 else None
            right = (rowAndColumn[0], rowAndColumn[1] + 1) if rowAndColumn[1] != len(hightmap[0]) - 1 else None

            pointsList = (up, down, left, right)

            doneList.append(rowAndColumn)
            size = 1
            for point in pointsList:
                if point != None and hightmap[point[0]][point[1]] != '9':
                    size += findBasinSize(point)
            return size

    lowPoints = []
    doneList = []
    basinSizes = []
    for row in range(len(hightmap)):
        for column in range(len(hightmap[0])):
            if isLowPoint(row, column):
                lowPoints.append(int(hightmap[row][column]))
                basinSizes.append(findBasinSize((row, column)))
    print('the basin sizes are:', basinSizes)

    while len(basinSizes) > 3:
        basinSizes.remove(min(basinSizes))
    return basinSizes[0] * basinSizes[1] * basinSizes[2]






if __name__ == '__main__':
    example = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    print('----- part one -----')
    test(True, example, 15)
    do_it(True, 'day9_data.txt') #not 1704
    print('----- part two -----')
    test(False, example, 1134)
    do_it(False, 'day9_data.txt')
