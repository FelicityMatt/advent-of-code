def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    pass


def part_two_code(lines: list):
    pass


if __name__ == '__main__':
    print()
    with open('day1/day1-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day1/day1-data.txt'
    answer_one = 24000
    answer_two = 45000

    print('----- part one -----')
    test(part_one_code, example, answer_one)
    print("the answer to part one is", do_it(part_one_code, filename))
    # print('----- part two -----')
    # test(part_two_code, example, answer_two)
    # print("the answer to part one is", do_it(part_two_code, filename))
    print()
