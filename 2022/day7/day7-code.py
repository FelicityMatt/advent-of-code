def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    line = lines[0]
    last_chars = ["", "", "", ""]
    i = 0
    num = 0

    for char in line:
        last_chars[i] = char
        num += 1
        all_unique = True
        for el in last_chars:
            if last_chars.count(el) > 1 or num < 4:
                all_unique = False
                break
        if all_unique:
            return num

        i = (i + 1) % 4

    return num


def part_two_code(lines: list):
    line = lines[0]
    last_chars = [""] * 14
    i = 0
    num = 0

    for char in line:
        last_chars[i] = char
        num += 1
        all_unique = True
        for el in last_chars:
            if last_chars.count(el) > 1 or num < 14:
                all_unique = False
                break
        if all_unique:
            return num

        i = (i + 1) % 14

    return num


if __name__ == '__main__':
    print()
    with open('day7/day7-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day7/day7-data.txt'
    answer_1 = 7
    answer_2 = 19

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
