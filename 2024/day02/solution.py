PART_ONE_SAMPLE_ANSWER = 2
PART_TWO_SAMPLE_ANSWER = 4
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
    reports = [list(map(int, x.split())) for x in lines]
    
    total_safe = 0
    for report in reports:
        is_safe = True
        if report[0] > report[1]:
            is_decreasing = True
        else:
            is_decreasing = False

        for i in range(1, len(report)):
            dif = report[i] - report[i-1]
            if is_decreasing and dif >= 0:
                is_safe = False
                break
            if not is_decreasing and dif <= 0:
                is_safe = False
                break
            if not (1 <= abs(dif) <= 3):
                is_safe = False
                break
        if is_safe:
            total_safe += 1


    return total_safe



def part_two_code(lines: list):
    reports = [list(map(int, x.split())) for x in lines]

    def check_report(report):
        if report[0] > report[1]:
            is_decreasing = True
        else:
            is_decreasing = False

        for i in range(1, len(report)):
            dif = report[i] - report[i-1]
            if is_decreasing and dif >= 0:
                return (False, i)
            if not is_decreasing and dif <= 0:
                return (False, i)
            if not (1 <= abs(dif) <= 3):
                return (False, i)
        return (True, -1)


    total_safe = 0

    for report in reports:
        is_safe, index = check_report(report)
        if is_safe:
            total_safe += 1
            continue
        
        for i in range(len(report)):
            copy = report[:]
            copy.pop(i)
            is_safe, _ = check_report(copy)
            if is_safe:
                total_safe += 1
                break

    return total_safe


if __name__ == '__main__':
    print('----- part one -----')
    compute_answer(SAMPLE_FILENAME, part_one_code, PART_ONE_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_one_code))
    print('----- part two -----')
    compute_answer(SAMPLE_FILENAME, part_two_code, PART_TWO_SAMPLE_ANSWER)
    print("part one answer:", compute_answer(REAL_DATA_FILENAME, part_two_code))
    print('--------------------')

