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
    #reading info into a dict containing all the different paths
    cavesDict = dict()
    for line in lines:
        path = line.split('-')
        for i in range(2):
            if path[i] in cavesDict.keys():
                cavesDict[path[i]].append(path[i-1])
            else:
                cavesDict[path[i]] = [path[i-1]]

    def travelFrom(currentPath):
        currentCave = currentPath[-1]
        if currentCave == 'end':
            return [currentPath]
        else:
            y = []
            for cave in cavesDict[currentCave]:
                pathAdded = currentPath[:]
                if cave not in currentPath or cave.isupper():
                    pathAdded.append(cave)
                    newPaths = travelFrom(pathAdded)
                    y += newPaths
            return y

    paths = travelFrom(['start'])

    return len(paths)


def part_two_code(lines: list):
    # reading info into a dict containing all the different paths
    cavesDict = dict()
    for line in lines:
        path = line.split('-')
        for i in range(2):
            if path[i] in cavesDict.keys():
                cavesDict[path[i]].append(path[i - 1])
            else:
                cavesDict[path[i]] = [path[i - 1]]

    def doublePresent(currentPath):
        for item in currentPath[1:]:
            if currentPath.count(item) > 1 and item.islower():
                return True
        return False


    def travelFrom(currentPath):
        currentCave = currentPath[-1]
        if currentCave == 'end':
            return [currentPath]
        else:
            y = []
            for cave in cavesDict[currentCave]:
                pathAdded = currentPath[:]
                if cave not in currentPath or cave.isupper():
                    pathAdded.append(cave)
                    newPaths = travelFrom(pathAdded)
                    y += newPaths
                elif not doublePresent(currentPath) and cave != 'start':
                    pathAdded.append(cave)
                    newPaths = travelFrom(pathAdded)
                    y += newPaths
            return y

    paths = travelFrom(['start'])


    return len(paths)


if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 10)
    do_it(True, 'day12_data.txt')
    print('----- part two -----')
    test(False, example, 36)
    do_it(False, 'day12_data.txt')
