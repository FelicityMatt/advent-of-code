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
    xValues = []
    yValues = []
    commands = []
    for line in lines:
        if ',' in line:
            x, y = map(int, line.split(','))
            xValues.append(x)
            yValues.append(y)
        elif '=' in line:
            commands.append(line)

    paper = []
    oneLine = ['.'] * (max(xValues) + 1)
    for _ in range(max(yValues) + 1):
        paper.append(oneLine[:])

    for i in range(len(xValues)):
        paper[yValues[i]][xValues[i]] = '#'

    # bigPaper = []
    # for lst in paper:
    #     bigPaper.append(''.join(lst))
    # print('\n'.join(bigPaper))

    for command in commands:
        if 'y' in command:
            rowNum = int(command[(command.index('=') + 1):])
            for i in range(rowNum): # first row num is 7 | goes through each row
                for j in range(len(paper[0])): #goes through each column
                    if paper[-1 - i][j] == '#':
                        paper[i][j] = '#'
            paper = paper[:rowNum]
        if 'x' in command:
            colNum = int(command[(command.index('=') + 1):])
            for i in range(len(paper)): # first row num is 7 | goes through each row
                for j in range(colNum): #goes through each column
                    if paper[i][-1 - j] == '#':
                        paper[i][j] = '#'
            paperCopy = paper[:]
            paper = []
            for row in paperCopy:
                paper.append(row[:colNum])

    bigPaper = []
    for lst in paper:
        bigPaper.append(''.join(lst))
    print('\n'.join(bigPaper))


    return sum(x.count('#') for x in paper)



def part_two_code(lines: list):
    pass


if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    #test(True, example, 17)
    do_it(True, 'day13_data.txt') # not 1050
    #print('----- part two -----')
    #test(False, example, 230)
    #do_it(False, 'day13_data.txt')

