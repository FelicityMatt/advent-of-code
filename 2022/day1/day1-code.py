def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    most_calories = 0
    cur_elf = 0

    for line in lines:
        if not line:
            if cur_elf > most_calories:
                most_calories = cur_elf
            cur_elf = 0
        else:
            cur_elf += int(line)

    return most_calories


def part_two_code(lines: list):
    cur_elf = 0
    elves = []

    for line in lines:
        if not line:
            elves.append(cur_elf)
            cur_elf = 0
        else:
            cur_elf += int(line)

    elves.append(cur_elf)
    elves.sort()

    return sum(elves[-3:])


if __name__ == '__main__':
    print()
    with open('day1/day1-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day1/day1-data.txt'
    answer_1 = 24000
    answer_2 = 45000

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
