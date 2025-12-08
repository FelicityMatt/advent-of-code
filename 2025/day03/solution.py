PART_ONE_SAMPLE_ANSWER = 357
PART_TWO_SAMPLE_ANSWER = 3121910778619
SAMPLE_FILENAME = "sample.txt"
REAL_DATA_FILENAME = "data.txt"

def compute_answer(filename: str, func, answer: int = None):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    
    res = func(lines)

    if answer is not None:
        print("sample answer is:", res)
        assert res == answer

    return res


def part_one_code(lines: list):

    count = 0

    for bank in lines:
        best_first = int(bank[0])
        best_second = int(bank[1])

        for i in range(2, len(bank)):
            num = int(bank[i])

            if num > best_first and i != len(bank)-1:
                best_first = num
                best_second = int(bank[i+1])
            elif num > best_second:
                best_second = num

        count += int(f"{best_first}{best_second}")


    return count

def part_two_code(lines: list):
    count = 0

    for bank in lines:
        best_lay = bank[:12]

        for i in range(12, len(bank)):
            num = int(bank[i])

            for j in range(-1, len(best_lay), -1):
                if num > bank[j]:

            #
            #
            # if num > best_first and i != len(bank)-1:
            #     best_first = num
            #     best_second = int(bank[i+1])
            # elif num > best_second:
            #     best_second = num
            #
        count += int("".join(best_lay))


    return count


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

