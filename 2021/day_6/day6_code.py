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
        lines = lines[0]
        # for part one
        if is_part_one:
            x = part_one_code(lines)
            print('the answer to part one is:', x)
        # for part two
        elif not is_part_one:
            x = part_two_code(lines)
            print('the answer to part two is:', x)


def part_one_code(line: str):
    lanternFish = list(map(int, line.split(',')))
    for day in range(80):
        for i in range(len(lanternFish[:])):
            if lanternFish[i] == 0:
                lanternFish[i] = 6
                lanternFish.append(8)
            else:
                lanternFish[i] -= 1
    return len(lanternFish)


def part_two_code(lines: list):
    initFish = list(map(int, lines.split(',')))
    lanternFish = [ initFish.count(num) for num in range(9)]

    DAYS = 256
    #after one day
    while DAYS > 0:
        zeros = lanternFish[0]
        lanternFish = lanternFish[1:]
        lanternFish.append(zeros)
        lanternFish[6] += zeros
        DAYS -= 1
    return(sum(lanternFish))




if __name__ == '__main__':
    example = '3,4,3,1,2'
    #print('----- part one -----')
    #test(True, example, 26)
    #do_it(True, 'day6_data.txt')
    print('----- part two -----')
    test(False, example, 26984457539)
    do_it(False, 'day6_data.txt')
