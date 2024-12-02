from stack_adt import ArrayStack

def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(get_data()))

def part_one_code(data: tuple[list, list[ArrayStack]]):
    lines, stacks = data
    print(stacks)

    for line in lines:
        # words = ["move", " 1", "from", "2", "to", "3"]
        words = line.split(" ")

        for i in range(int(words[1])):
            item = stacks[int(words[3]) - 1].pop()
            stacks[int(words[5]) - 1].push(item)

    letters = []
    for stack in stacks:
        letters.append(stack.pop())

    return "".join(letters)


def part_two_code(data: tuple[list, list[ArrayStack]]):
    lines, stacks = data
    print(stacks)

    for line in lines:
        # words = ["move", " 1", "from", "2", "to", "3"]
        words = line.split(" ")

        temp = ArrayStack(int(words[1]))
        for _ in range(int(words[1])):
            temp.push(stacks[int(words[3]) - 1].pop())

        for _ in range(int(words[1])):
            stacks[int(words[5]) - 1].push(temp.pop())
    
    letters = []
    for stack in stacks:
        letters.append(stack.pop())

    return "".join(letters)


def get_sample_stack():
    stacks = []
    elements = [["N", "Z"], ["D", "C", "M"], ["P"]]

    for el in elements:
        stack = ArrayStack(6)
        for i in range(len(el)-1, -1, -1):
            stack.push(el[i])
        stacks.append(stack)

    with open('day5/day5-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    return (example, stacks)

def get_data():
    stacks = []
    with open('day5/day5-stacks', 'r') as fileref:
        data = [line.strip() for line in fileref]

    elements = []
    for line in data:
        el = []
        for char in line:
            el.append(char)
        elements.append(el)
    print(elements)

    for el in elements:
        stack = ArrayStack(50)
        for i in range(len(el)-1, -1, -1):
            stack.push(el[i])
        stacks.append(stack)

    with open('day5/day5-data.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    return (example, stacks)


if __name__ == '__main__':
    print()
    with open('day5/day5-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day5/day5-data.txt'
    answer_1 = "CMZ"
    answer_2 = "MCD"

    print('----- part one -----')
    test(part_one_code, get_sample_stack(), answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, get_sample_stack(), answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
