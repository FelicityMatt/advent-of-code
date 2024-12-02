def get_movements(lines:list) -> tuple:
    horizontal_position = 0
    depth = 0
    for line in lines:
        if 'forward' in line:
            horizontal_position += int(line[-1])
        elif 'down' in line:
            depth += int(line[-1])
        elif 'up' in line:
            depth -= int(line[-1])
    return (horizontal_position, depth)

def test_part_one():
    example = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    x = get_movements(example)
    assert x == (15, 10)
    assert x[0] * x[1] == 150
    print(x)

def do_part_one():
    with open('day2_data.txt', 'r') as fileref:
        lines = [line.strip() for line in fileref]
        y = get_movements(lines)
        print('the position and depth is:', y)
        print('times each other is:', y[0] * y[1])


def now_with_aim(lines:list) -> tuple:
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in lines:
        if 'forward' in line:
            x = int(line[-1])
            horizontal_position += x
            depth += x * aim
        elif 'down' in line:
            aim += int(line[-1])
        elif 'up' in line:
            aim -= int(line[-1])
    return (horizontal_position, depth)

def test_part_two():
    example = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    x = now_with_aim(example)
    assert x == (15, 60)
    assert x[0] * x[1] == 900
    print(x)

def do_part_two():
    with open('day2_data.txt', 'r') as fileref:
        lines = [line.strip() for line in fileref]
        y = now_with_aim(lines)
        print('the position and depth is:', y)
        print('times each other is:', y[0] * y[1])

if __name__ == '__main__':
    print('----- part one -----')
    test_part_one()
    do_part_one()
    print('----- part two -----')
    test_part_two()
    do_part_two()


