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

    sums = []

    for i in range(7):
        #print(lines[i])

        print("\n--- new packet --- ")

        binary = str(bin(int(lines[i],16)))[2:].zfill(len(lines[i]) * 4)

        print(binary)
        print("hex representation:", hex(int(binary, 2)))

        versions = list()
        
        read_packet(binary, versions)

        sums.append(sum(versions))
        print("--- sum ---")
        print(sums)
        print("-----------")

    return sums

# 000 000 0 001010100000100 | 001 100 10011 00110 | 101 001 1 00000000010 110110100000000010110100001110001000011100010011100011110111001011110100111101100101001011001100000000010101100111111110000001011110100000000010101100111010010101110010110110111011

def read_packet(binary: str, version_nums: list):
    print()
    print("--- reading a packet ---")
    print("binary start:", binary[:40])
    #print("hex representation:", hex(int(binary, 2)))
    print("current sum:", sum(version_nums))

    print("length of the string:", len(binary))
    assert len(binary) > 6, "this binary string is invalid"

    print(binary[0:3])
    version = int(binary[0:3], 2)
    print("Version:", version)
    print(binary[3:6])
    type_id = int(binary[3:6], 2)
    print("Type ID:", type_id)

    size = 0
    
    version_nums.append(version)

    # a literal number
    if type_id == 4:
        num, size = read_literal_value(binary[6:])
        size += 6
        return (num, size)

    # else an operator
    length_type_id = int(binary[6])
    print("Length Type ID:", length_type_id)
    size += 7
    numbers = []

    # 1 -> 11 bits : number of sub-packets immediately contained
    if length_type_id:
        size += 11
        num_sub_packets = int(binary[7:18], 2)
        print(binary[7:18])
        print("number of sub-packets:", num_sub_packets)

        packets = binary[18:]
        assert num_sub_packets < len(packets), f"there cannot be that many sub-packets, {num_sub_packets} is greater than {len(packets)}"
        i = 0
        for _ in range(num_sub_packets):
            res = read_packet(packets[i:], version_nums)
            size += res[1]
            numbers.append(res[0])
            print(res)                   
            i += res[1]
    

    # 0 -> 15 bits : total length in bits
    else:
        size += 15
        total_length = int(binary[7:22], 2)
        print(binary[7:22])
        print("total number of bits:", total_length)

        packets = binary[22:]
        assert total_length < len(packets), f"there cannot be that many bits in this packet, {total_length} is greater than {len(packets)}"

        i = 0
        while i < total_length:
            res = read_packet(packets[i:], version_nums)
            size += res[1]
            numbers.append(res[0])
            print(res)                    
            i += res[1]
    
    num = numbers[0]

    # use the operator:
    # sum packets
    if type_id == 0:
        num = sum(numbers)
    # product packets
    elif type_id == 1:
        for i in range(1, len(numbers)):
            num = num * numbers[i]
    # minimum packets
    elif type_id == 2:
        num = min(numbers)
    # maximum packets
    elif type_id == 3:
        num = max(numbers)
    # greater than packets
    elif type_id == 5:
        num = int(numbers[0] > numbers[1])
    # less than packets
    elif type_id == 6:
        num = int(numbers[0] < numbers[1])
    # equal to packets
    elif type_id == 7:
        num = int(numbers[0] == numbers[1])
    else:
        raise ValueError("type id is invalid")


    return (num, size)


def read_literal_value(binary: str) -> tuple[int, int]:
    num_list = list()
    for i in range(0, len(binary), 5):
        bit = binary[i + 1:i + 5]
        num_list.append(bit)
        if binary[i] == '0':
            num_bits = (i + 5) 
            break
    string_num = ''.join(num_list)

    # returns a tuple of (literal value, length of packet)
    return (int(string_num, 2), num_bits)


def part_two_code(lines: list):
    results = list()

    for i in range(0, len(lines)):
    #print(lines[i])

        print("\n--- new packet --- ")

        binary = str(bin(int(lines[i],16)))[2:].zfill(len(lines[i]) * 4)

        print(binary)
        print("hex representation:", hex(int(binary, 2)))

        results.append(read_packet2(binary)[0])

    return results


def read_packet2(binary: str):
    print()
    print("--- reading a packet ---")
    print("binary start:", binary[:40])
    #print("hex representation:", hex(int(binary, 2)))


    print("length of the string:", len(binary))
    assert len(binary) > 6, "this binary string is invalid"

    print(binary[0:3])
    version = int(binary[0:3], 2)
    print("Version:", version)
    print(binary[3:6])
    type_id = int(binary[3:6], 2)
    print("Type ID:", type_id)

    size = 0

    # a literal number
    if type_id == 4:
        num, size = read_literal_value(binary[6:])
        size += 6
        return (num, size)

    # else an operator
    length_type_id = int(binary[6])
    print("Length Type ID:", length_type_id)
    size += 7
    numbers = []

    # 1 -> 11 bits : number of sub-packets immediately contained
    if length_type_id:
        size += 11
        num_sub_packets = int(binary[7:18], 2)
        print(binary[7:18])
        print("number of sub-packets:", num_sub_packets)

        packets = binary[18:]
        assert num_sub_packets < len(packets), f"there cannot be that many sub-packets, {num_sub_packets} is greater than {len(packets)}"
        i = 0
        for _ in range(num_sub_packets):
            res = read_packet2(packets[i:])
            size += res[1]
            numbers.append(res[0])
            print(res)                   
            i += res[1]
    

    # 0 -> 15 bits : total length in bits
    else:
        size += 15
        total_length = int(binary[7:22], 2)
        print(binary[7:22])
        print("total number of bits:", total_length)

        packets = binary[22:]
        assert total_length < len(packets), f"there cannot be that many bits in this packet, {total_length} is greater than {len(packets)}"

        i = 0
        while i < total_length:
            res = read_packet2(packets[i:])
            size += res[1]
            numbers.append(res[0])
            print(res)                    
            i += res[1]
    
    num = numbers[0]

    # use the operator:
    # sum packets
    if type_id == 0:
        num = sum(numbers)
    # product packets
    elif type_id == 1:
        for i in range(1, len(numbers)):
            num = num * numbers[i]
    # minimum packets
    elif type_id == 2:
        num = min(numbers)
    # maximum packets
    elif type_id == 3:
        num = max(numbers)
    # greater than packets
    elif type_id == 5:
        num = int(numbers[0] > numbers[1])
    # less than packets
    elif type_id == 6:
        num = int(numbers[0] < numbers[1])
    # equal to packets
    elif type_id == 7:
        num = int(numbers[0] == numbers[1])
    else:
        raise ValueError("type id is invalid")


    return (num, size)


    


if __name__ == '__main__':
    print()
    with open('day_16/sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, [6, 9, 14, 16, 12, 23, 31])
    #do_it(True, 'day_16/day16_data.txt')
    print('----- part two -----')
    #test(False, example, [3, 54, 7, 9, 1, 0, 0, 1])
    do_it(False, 'day_16/day16_data.txt')
    print()
