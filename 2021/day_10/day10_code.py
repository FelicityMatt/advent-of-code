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
    openBrackets = ['(', '[', '{', '<']
    closedBrackets = [')', ']', '}', '>']

    points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    pointsTotal = 0

    for line in lines:
        brackets =[]
        for char in line:
            if char in openBrackets:
                brackets.append(char)
            elif char in closedBrackets:
                if closedBrackets.index(char) != openBrackets.index(brackets[-1]):
                    illegalChar = char
                    pointsTotal += points_dict[char]
                    break
                else:
                    brackets = brackets[:-1]
    return pointsTotal


def part_two_code(lines: list):
    openBrackets = ['(', '[', '{', '<']
    closedBrackets = [')', ']', '}', '>']

    points_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    pointsList = []

    for line in lines:
        brackets = []
        isIncomplete = False
        pointsTotal = 0
        for char in line:
            if char in openBrackets:
                brackets.append(char)
            elif char in closedBrackets:
                if closedBrackets.index(char) != openBrackets.index(brackets[-1]):
                    isIncomplete = True
                    break
                else:
                    brackets = brackets[:-1]
        if not isIncomplete:
            neededBrackets = [closedBrackets[openBrackets.index(bracket)] for bracket in reversed(brackets)]
            for bracket in neededBrackets:
                pointsTotal = pointsTotal * 5 + points_dict[bracket]
            pointsList.append(pointsTotal)
    return sorted(pointsList)[int(len(pointsList)/2)]


if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 26397)
    do_it(True, 'day10_data.txt')
    print('----- part two -----')
    test(False, example, 288957)
    do_it(False, 'day10_data.txt')
