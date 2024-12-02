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
    # 1 -> cf (2 segments)
    # 4 -> bcdf (4 segments)
    # 7 -> acf (3 segments)
    # 8 -> abcdefg (7 segments)
    totalDigits = 0
    for line in lines:
        data = line.split('|')
        digits = [x for x in data[1].strip().split(' ') if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7]
        totalDigits += len(digits)
    return totalDigits



def part_two_code(lines: list):
    # 1 -> cf (2 segments)
    # 4 -> bcdf (4 segments)
    # 7 -> acf (3 segments)
    # 8 -> abcdefg (7 segments)
    totalSum = 0
    for line in lines:
        data = line.split('|')
        digits = [x for x in data[1].strip().split(' ')]
        randomDigits = [x for x in data[0].strip().split(' ')]
        allLines = 'abcdefg'

        lengths = [2,4,3,7]
        oneSevenFourEight = sorted([x for x in randomDigits if len(x) in lengths], key=len)

        code = dict()
        cf = [x for x in oneSevenFourEight[1] if x in oneSevenFourEight[0]]

        for x in oneSevenFourEight[1]:
            if x not in oneSevenFourEight[0]:
                code['a'] = x

        bd = [x for x in oneSevenFourEight[2] if x not in cf]

        twoThreeFive = [x for x in randomDigits if len(x) == 5]

        adg = [x for x in twoThreeFive[0] if x in twoThreeFive[1] and x in twoThreeFive[2]]

        for x in adg:
            if x in bd:
                code['d'] = x
                bd.remove(x)
                adg.remove((x))
                code['b'] = bd[0]
                adg.remove(code['a'])
                code['g'] = adg[0]

        for num in twoThreeFive:
            if code['b'] in num:
                for letter in num:
                    if letter not in code.values():
                        code['f'] = letter
                        cf.remove(letter)
                        code['c'] = cf[0]

        code['e'] = list(filter(lambda x: x not in code.values(), allLines))[0]

        finalDigits = ''
        lengthDigits = {2: '1', 4: '4', 3: '7', 7: '8'}
        for digit in digits:
            if len(digit) in lengthDigits.keys():
                finalDigits += lengthDigits[len(digit)]
            elif len(digit) == 5:       #for 2, 5 and 3
                if code['e'] in digit:
                    finalDigits += '2'
                elif code['b'] in digit:
                    finalDigits += '5'
                else:
                    finalDigits += '3'
            else:           #for 0, 6 and 9
                if code['d'] not in digit:
                    finalDigits += '0'
                elif code['c'] not in digit:
                    finalDigits += '6'
                elif code['e'] not in digit:
                    finalDigits += '9'

        totalSum += int(finalDigits)

    return totalSum










if __name__ == '__main__':
    with open('sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 26)
    do_it(True, 'day8_data.txt')
    print('----- part two -----')
    #example = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    test(False, example, 61229)
    do_it(False, 'day8_data.txt')
