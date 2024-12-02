def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    directory = {"/": 0}
    cur_dir = "/"
    keys = []

    for line in lines:
        # it is a command to move around
        if line[0:4] == "$ cd":
            # moves to outermost directory
            if line[5:] == "/":
                cur_dir = "/"
            # moves out one directory
            elif line[5:] == "..":
                split = cur_dir.split('/')[:-2]
                cur_dir = "/".join(split) + "/"
         
            # moves to the specified directory
            else:
                moving_to = line[5:]
                cur_dir = cur_dir + moving_to + "/"

        elif line[0:4] == "$ ls":
            pass

        # it is a list of dir contents
        else:
            if line[0:3] == "dir":
                keys.append(line[4:])
                new_dir = cur_dir + line[4:] + "/"
                directory[new_dir] = 0

            else:
                size = int(line.split(" ")[0])

                directory[cur_dir] += size

    # print(keys)
    # print(directory)

    total = 0

    for folder in directory.keys():
        dir_total = 0
        for key in directory.keys():
            if folder in key:
                dir_total += directory[key]
        if dir_total <= 100000:
            total += dir_total

    # not 1345579      
    return total



def part_two_code(lines: list):
    directory = {"/": 0}
    cur_dir = "/"
    keys = []

    for line in lines:
        # it is a command to move around
        if line[0:4] == "$ cd":
            # moves to outermost directory
            if line[5:] == "/":
                cur_dir = "/"
            # moves out one directory
            elif line[5:] == "..":
                split = cur_dir.split('/')[:-2]
                cur_dir = "/".join(split) + "/"
         
            # moves to the specified directory
            else:
                moving_to = line[5:]
                cur_dir = cur_dir + moving_to + "/"

        elif line[0:4] == "$ ls":
            pass

        # it is a list of dir contents
        else:
            if line[0:3] == "dir":
                keys.append(line[4:])
                new_dir = cur_dir + line[4:] + "/"
                directory[new_dir] = 0

            else:
                size = int(line.split(" ")[0])

                directory[cur_dir] += size

    # print(keys)
    # print(directory)
    space_available = 70000000

    space_needed = 30000000

    free_space = space_available - sum(directory.values())
    print("total space free:", free_space)

    total = 0
    delete_dir = 30000000

    for folder in directory.keys():
        dir_total = 0
        for key in directory.keys():
            if folder in key:
                dir_total += directory[key]

        print(free_space + dir_total)

        if free_space + dir_total >= space_needed and dir_total < delete_dir:
            print(dir_total, "was greater")
            delete_dir = dir_total

    # not 1345579      
    return delete_dir


if __name__ == '__main__':
    print()
    with open('day8/day8-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day8/day8-data.txt'
    answer_1 = 95437
    answer_2 = 24933642

    print('----- part one -----')
    test(part_one_code, example, answer_1)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_2)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
