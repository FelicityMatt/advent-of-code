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


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def is_x(self, x_value):
        return self.x == x_value

    def is_y(self, y_value):
        return self.y == y_value

    def __str__(self):
        return f'({self.x},{self.y})'


def reading_data(lines):
    """ reading data for part one """
    points_dict = dict()
    for line in lines:
        str_points = line.split(' ')
        str_points.remove('->') # -> ['0,9', '2,9']
        points = [chars.split(',') for chars in str_points] # -> [['0','9'], ['2','9']]
        tup_points = [Point(chars[0], chars[1]) for chars in points] # -> [Point, Point]
        if tup_points[0].x == tup_points[1].x or tup_points[0].y == tup_points[1].y:
            points_dict[tup_points[0]] = tup_points[1]
    return points_dict

def reading_data2(lines):
    """ reading data for part two """
    points_dict = dict()
    for line in lines:
        str_points = line.split(' ')
        str_points.remove('->') # -> ['0,9', '2,9']
        points = [chars.split(',') for chars in str_points] # -> [['0','9'], ['2','9']]
        tup_points = [Point(chars[0], chars[1]) for chars in points] # -> [Point, Point]
        if tup_points[0].x == tup_points[1].x or tup_points[0].y == tup_points[1].y:
            points_dict[tup_points[0]] = tup_points[1]
        elif abs(tup_points[0].x - tup_points[1].x) == abs(tup_points[0].y - tup_points[1].y):
            points_dict[tup_points[0]] = tup_points[1]
    return points_dict

def part_one_code(lines: list):
    points_dict = reading_data(lines)
    points_list = []
    dupes = 0
    dupes_list = []
    for point in points_dict.keys():
        if point.x == points_dict[point].x:  # the x value is the same
            x = point.x
            y_start = min(point.y, points_dict[point].y)
            y_end = max(point.y, points_dict[point].y)
            for y in range(y_start, y_end + 1):
                if (x, y) in points_list and (x, y) not in dupes_list:
                    dupes += 1
                    dupes_list.append((x, y))
                else:
                    points_list.append((x, y))
        elif point.y == points_dict[point].y:  # the y value is the same
            y = point.y
            x_start = min(point.x, points_dict[point].x)
            x_end = max(point.x, points_dict[point].x)
            for x in range(x_start, x_end + 1):
                if (x, y) in points_list and (x, y) not in dupes_list:
                    dupes += 1
                    dupes_list.append((x, y))
                else:
                    points_list.append((x, y))
    return dupes


def part_two_code(lines: list):
    points_dict = reading_data2(lines)
    points_list = []
    dupes = 0
    dupes_list = []
    for point in points_dict.keys():
        if point.x == points_dict[point].x:  # the x value is the same
            x = point.x
            y_start = min(point.y, points_dict[point].y)
            y_end = max(point.y, points_dict[point].y)
            for y in range(y_start, y_end + 1):
                if (x, y) in points_list and (x, y) not in dupes_list:
                    dupes += 1
                    dupes_list.append((x, y))
                else:
                    points_list.append((x, y))
        elif point.y == points_dict[point].y:  # the y value is the same
            y = point.y
            x_start = min(point.x, points_dict[point].x)
            x_end = max(point.x, points_dict[point].x)
            for x in range(x_start, x_end + 1):
                if (x, y) in points_list and (x, y) not in dupes_list:
                    dupes += 1
                    dupes_list.append((x, y))
                else:
                    points_list.append((x, y))
        elif abs(point.x - points_dict[point].x) == abs(point.y - points_dict[point].y):
            x_start = min(point.x, points_dict[point].x)
            x_end = max(point.x, points_dict[point].x)
            if point.is_x(x_start): #the point key is the left most x
                y_start = point.y
                y_end = points_dict[point].y
            else: #the point value is the left most x
                y_start = points_dict[point].y
                y_end = point.y
            y = y_start
            for x in range(x_start, x_end + 1):
                if (x, y) in points_list and (x, y) not in dupes_list:
                    dupes += 1
                    dupes_list.append((x, y))
                else:
                    points_list.append((x, y))
                if y_start > y_end:
                    y -= 1
                elif y_start < y_end:
                    y += 1


    return dupes


if __name__ == '__main__':
    with open('sample_data.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]
    print('----- part one -----')
    test(True, example, 5)
    #do_it(True, 'day5_data.txt')
    print('----- part two -----')
    test(False, example, 12)
    do_it(False, 'day5_data.txt')
