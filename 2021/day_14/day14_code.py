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
    polymer = [x for x in lines[0]]
    pairRules = dict()
    for line in lines:
        if '->' in line:
            x, y = line.split(' -> ')
            pairRules[x] = y

    for _ in range(10):
        polymerDupe = []
        for i in range(len(polymer) - 1):
            polymerDupe.append(polymer[i])
            pair = polymer[i] + polymer[i+1]
            polymerDupe.append(pairRules[pair])
        polymerDupe.append(polymer[-1])
        polymer = polymerDupe

    biggest = max(set(polymer), key=polymer.count)
    smallest = min(set(polymer), key=polymer.count)
    return polymer.count(biggest) - polymer.count(smallest)


def part_two_code(lines: list):
    polymerInit = [x for x in lines[0]]
    pairRules = dict()
    for line in lines:
        if '->' in line:
            x, y = line.split(' -> ')
            pairRules[x] = y

    # creating the polymer dictionary
    pairs = list(pairRules.keys())
    zeros = [0] * len(pairs)
    polymer = dict(zip(pairs, zeros))

    # finding the initial values for the polymer dictionary
    for i in range(len(polymerInit) - 1):
        polymer[polymerInit[i] + polymerInit[i + 1]] += 1

    for _ in range(40):
        new_dict = dict(zip(pairs, zeros))
        for pair in polymer:
            x, y = [x for x in pair]
            z = pairRules[pair]
            new_dict[x + z] += polymer[pair]
            new_dict[z + y] += polymer[pair]
        polymer = new_dict.copy()

    letters = dict()
    for pair in polymer:
        if pair[0] not in letters.keys():
            letters[pair[0]] = polymer[pair]
        else:
            letters[pair[0]] += polymer[pair]

    letters[polymerInit[-1]] += 1

    print(letters)

    maxVal = max(letters.values())
    minVal = min(letters.values())

    return maxVal - minVal

if __name__ == '__main__':
    with open('sample', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 1588)
    #do_it(True, 'day14_data.txt')
    print('----- part two -----')
    test(False, example, 2188189693529)
    do_it(False, 'day14_data.txt')
