def part_one_code(lines:list):
    gamma_ray = ''
    for i in range(len(lines[0])):
        zeros = len([x[i] for x in lines if x[i] == '0'])
        ones = len(lines) - zeros
        if zeros > ones:
            gamma_ray += '0'
        elif ones > zeros:
            gamma_ray += '1'

    epsilon_rate = ''.join(['0' if x == '1' else '1' for x in gamma_ray])
    print((gamma_ray, epsilon_rate))

    return int(gamma_ray,2) * int(epsilon_rate,2)


def test(is_part_one:bool, example:list, answer:int):
    #test for part one
    if is_part_one == True:
        x = part_one_code(example)
        print('sample answer is:', x)
        assert x == answer
    #test for part two
    elif is_part_one == False:
        x = part_two_code(example)
        print('sample answer is:', x)
        assert x == answer


def do_it(is_part_one, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        #for part one
        if is_part_one == True:
            x = part_one_code(lines)
            print('the answer to part one is:', x)
        #for part two
        elif is_part_one == False:
            x = part_two_code(lines)
            print('the answer to part two is:', x)


def part_two_code(lines:list):
    def get_oxygen(i:int, lines:list) -> str:
        if len(lines) == 1:
            return lines
        else:
            zeros = [x for x in lines if x[i] == '0']
            ones = [x for x in lines if x[i] == '1']
            if len(zeros) > len(ones):
                return get_oxygen(i+1, zeros)
            elif len(ones) >= len(zeros):
                return get_oxygen(i + 1, ones)

    def get_CO2(i:int, lines:list) -> str:
        if len(lines) == 1:
            return lines
        else:
            zeros = [x for x in lines if x[i] == '0']
            ones = [x for x in lines if x[i] == '1']
            if len(zeros) <= len(ones):
                return get_CO2(i+1, zeros)
            elif len(ones) < len(zeros):
                return get_CO2(i + 1, ones)

    oxygen_gen_rating = int((get_oxygen(0,lines))[0], 2)
    CO2_scrubber_rating = int((get_CO2(0,lines))[0],2)
    return oxygen_gen_rating * CO2_scrubber_rating



if __name__ == '__main__':
    example = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    print('----- part one -----')
    test(True, example, 198)
    do_it(True, 'day3_data.txt')
    print('----- part two -----')
    test(False, example, 230)
    do_it(False, 'day3_data.txt')


