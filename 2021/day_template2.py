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
    pass


def part_two_code(lines: list):
    pass


if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 198)
    #do_it(True, 'day3_data.txt')
    #print('----- part two -----')
    #test(False, example, 230)
    #do_it(False, 'day3_data.txt')
