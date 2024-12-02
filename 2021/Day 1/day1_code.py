# part 1

def num_of_depth_increases(lines:list) -> int:
    return len(['increase' for index in range(len(lines)) if lines[index - 1] < lines[index]])


# part 2

get_sum = (lambda lst, i: lst[i - 1] + lst[i] + lst[i + 1])

def get_triplet_differences(lines:list) -> int:
    total = 0
    for i in range(1, len(lines)-2):
        sum_1 = get_sum(lines, i)
        sum_2 = get_sum(lines, i + 1)
        if sum_1 < sum_2:
            total += 1
    print('total number of triplet increases is:', total)
    return total

if __name__ == '__main__':
    with open('day1_data.txt', 'r') as fileref:
        lines = [int(line.strip()) for line in fileref]
        print(num_of_depth_increases(lines))
        get_triplet_differences((lines))


