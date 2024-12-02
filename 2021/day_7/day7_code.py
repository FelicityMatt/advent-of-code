def test(is_part_one: bool, example: str, answer: int):
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
        line = lines[0]
        # for part one
        if is_part_one:
            x = part_one_code(line)
            print('the answer to part one is:', x)
        # for part two
        elif not is_part_one:
            x = part_two_code(line)
            print('the answer to part two is:', x)


def part_one_code(line: str):
    crabPos = list(map(int, line.split(',')))
    minFuel = sum(abs(crab - 0) for crab in crabPos)
    for point in range(max(crabPos) + 1):
        fuel = sum(abs(crab - point) for crab in crabPos)
        minFuel = min(minFuel, fuel)
    return minFuel


def part_two_code(line: str):
    crabPos = list(map(int, line.split(',')))
    minFuel = sum(sum(range(abs(crab - 0) + 1)) for crab in crabPos)
    for point in range(min(crabPos), max(crabPos) + 1):
        fuel = 0
        for crab in crabPos:
            dif = abs(crab - point)
            fuel += sum(range(dif + 1))
        minFuel = min(minFuel, fuel)
    return minFuel




if __name__ == '__main__':
    example = '16,1,2,0,4,2,7,1,2,14'
    print('----- part one -----')
    test(True, example, 37)
    do_it(True, 'day7_data.txt')
    print('----- part two -----')
    test(False, example, 168)
    do_it(False, 'day7_data.txt')
