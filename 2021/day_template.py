def part_one_code(lines:list):
    pass

def test_part_one():
    example = []
    x = part_one_code(example)
    assert x == y
    print(x)

def do_part_one():
    with open('day3_data.txt', 'r') as fileref:
        lines = [line.strip() for line in fileref]
        y = part_one_code(lines)
        print(y)


def part_two_code(lines:list):
    pass

def test_part_two():
    example = []
    x = part_two_code(example)
    assert x == y
    print(x)

def do_part_two():
    with open('day3_data.txt', 'r') as fileref:
        lines = [line.strip() for line in fileref]
        y = part_two_code(lines)
        print(y)

if __name__ == '__main__':
    print('----- part one -----')
    test_part_one()
    do_part_one()
    print('----- part two -----')
    test_part_two()
    do_part_two()


