def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    # rock paper scissors
    opponent = ["A", "B", "C"]
    you = ["X", "Y", "Z"]

    total = 0

    for line in lines:
        o, y = line.split(" ")

        total += you.index(y) + 1

        if opponent.index(o) == (you.index(y) - 1) % 3:
            total += 6
        
        if opponent.index(o) == you.index(y) % 3:
            total += 3

    return total



def part_two_code(lines: list):
    # lose draw win
    #  0     1     2
    # rock paper scissors

    # win 0 -> 1
    # 1 -> 2
    # 2 -> 0

    opponent = ["A", "B", "C"]
    you = ["X", "Y", "Z"]

    total = 0

    for line in lines:
        o, y = line.split(" ")

        # lose
        if y == "X":
            total += (opponent.index(o) + 2) % 3 + 1

        # draw
        if y == "Y":
            total += opponent.index(o) + 1
            total += 3

        # win
        if y == "Z":
            total += (opponent.index(o) + 1) % 3 + 1
            total += 6
        
    return total


if __name__ == '__main__':
    print()
    with open('day2/day2-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day2/day2-data.txt'
    answer_1 = 15
    answer_2 = 12

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
