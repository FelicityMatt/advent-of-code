def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    alphabet = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sum_of = 0

    for line in lines:
        half_point = len(line) // 2

        first_half = line[:half_point]
        second_half = line[half_point:]

        for l in first_half:
            if l in second_half:
                sum_of += alphabet.index(l)
                break

    return sum_of



def part_two_code(lines: list):
    alphabet = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sum_of = 0

    for i in range(0, len(lines), 3):
        for l in lines[i]:
            if l in lines[i+1] and l in lines[i+2]:
                sum_of += alphabet.index(l)
                break
    return sum_of



if __name__ == '__main__':
    print()
    with open('day3/day3-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day3/day3-data.txt'
    answer_1 = 157
    answer_2 = 70

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
