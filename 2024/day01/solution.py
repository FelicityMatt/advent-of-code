PART_ONE_TEST_ANSWER = 11
PART_TWO_TEST_ANSWER = 31

def test(is_part_one: bool, example: list, answer: int):
    # test for part one
    if is_part_one:
        x = part_one_code(example)
        print('sample answer is:', x)
        assert x == answer
    # test for part two
    elif not is_part_one:
        x = part_two_code(example)
        print('sample answer is:', x)
        assert x == answer


def do_it(is_part_one, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        # for part one
        if is_part_one:
            x = part_one_code(lines)
            print('the answer to part one is:', x)
        # for part two
        elif not is_part_one:
            x = part_two_code(lines)
            print('the answer to part two is:', x)


def part_one_code(lines: list):
    tuples = [line.split() for line in lines]
    
    first = [int(x[0]) for x in tuples]
    second = [int(x[1]) for x in tuples]
    
    first.sort()
    second.sort()
        
    total_dist = 0
    
    for _ in range(len(first)):
        total_dist += abs(first[0] - second[0])
        first = first[1:]
        second = second[1:]
        
    return total_dist


def part_two_code(lines: list):
    tuples = [line.split() for line in lines]
    
    first = [int(x[0]) for x in tuples]
    second = [int(x[1]) for x in tuples]
    
    score = 0
    
    for id in first:
        score += id * second.count(id)

            
    return score
    
    


if __name__ == '__main__':
    with open('sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, PART_ONE_TEST_ANSWER)
    do_it(True, 'data.txt')
    print('----- part two -----')
    test(False, example, PART_TWO_TEST_ANSWER)
    do_it(False, 'data.txt')

