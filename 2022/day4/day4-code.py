def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    total = 0

    for line in lines:
        # array of each of the min/max numbers
        elves = [x.split('-') for x in line.split(",")]
        elves = [int(x) for l in elves for x in l]

        # if the second is contained in the first
        if (elves[3] <= elves[1] and elves[0] <= elves[2] or 
                elves[3] >= elves[1] and elves[0] >= elves[2]):
            # if the first is contained in the second
            total += 1

    return total  



def part_two_code(lines: list):
    total = 0

    for line in lines:
        # array of each of the min/max numbers
        elves = [x.split('-') for x in line.split(",")]
        elves = [int(x) for l in elves for x in l]

        for i in range(elves[0], elves[1] + 1):
            if elves[2] <= i <= elves[3]:
                total += 1
                break

    return total
    


if __name__ == '__main__':
    print()
    with open('day4/day4-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day4/day4-data.txt'
    answer_1 = 2
    answer_2 = 4

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
