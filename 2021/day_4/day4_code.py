def test(is_part_one: bool, example: list, answer: int):
    # test for part one
    if is_part_one:
        x = part_one_code(example)
        print('sample answer is:', x)
        assert x == answer
    # test for part two
    else:
        x = part_two_code(example)
        print('sample answer is:', x)
        assert x == answer


def do_it(is_part_one, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line[:-1] for line in fileref]
        # for part one
        if is_part_one:
            x = part_one_code(lines)
            print('the answer to part one is:', x)
        # for part two
        else:
            x = part_two_code(lines)
            print('the answer to part two is:', x)

def part_one_code(lines: list):
    def get_boards(lines):
        temp_boards = []
        cur_board = []
        for line in lines:
            if line == '':
                temp_boards.append(cur_board)
                cur_board = []
            elif line != lines[0]:
                cur_board.append([line[i:i + 2].strip() for i in range(0, len(line), 3)])
        temp_boards.append(cur_board)
        return temp_boards[1:]

    def go_through_nums():
        for num in numbers_called:
            for board in boards:
                for row in board:
                    for i in range(len(row)):
                        if row[i] == num:
                            row[i] = '*'
            for board in boards:
                if check_if_one(board):
                    return (num, board)

    def check_if_one(board):
        for row in board:
            if row.count('*') == 5:
                return True
        for i in range(len(board)):
            total_stars = len([row[i] for row in board if row[i] == '*'])
            if total_stars == 5:
                return True
        return False


    numbers_called = lines[0].split(',')
    boards = get_boards(lines)
    winners = go_through_nums()
    score = 0
    for row in winners[1]:
        score += sum(int(x) for x in row if x.isdigit())

    return score * int(winners[0])


def check_if_won(board):
    for row in board:
        if row.count('*') == 5:
            return True
    for i in range(len(board)):
        total_stars = len([row[i] for row in board if row[i] == '*'])
        if total_stars == 5:
            return True
    return False

def part_two_code(lines: list):
    def get_boards(lines):
        temp_boards = []
        cur_board = []
        for line in lines:
            if line == '':
                temp_boards.append(cur_board)
                cur_board = []
            elif line != lines[0]:
                cur_board.append([line[i:i + 2].strip() for i in range(0, len(line), 3)])
        temp_boards.append(cur_board)
        return temp_boards[1:]

    def go_through_nums():
        for num in numbers_called:
            for board in boards[:]:
                for row in board:
                    for i in range(len(row)):
                        if row[i] == num:
                            row[i] = '*'

                if check_if_won(board):
                    if len(boards) != 1:
                        boards.remove(board)
                    elif len(boards) == 1:
                        return(num, boards[0])

    def check_if_won(board):
        for row in board:
            if row.count('*') == 5:
                return True
        for i in range(len(board)):
            total_stars = len([row[i] for row in board if row[i] == '*'])
            if total_stars == 5:
                return True
        return False

    numbers_called = lines[0].split(',')
    boards = get_boards(lines)

    loser_deets = go_through_nums()
    score = 0
    for row in loser_deets[1]:
        score += sum(int(x) for x in row if x.isdigit())

    return score * int(loser_deets[0])


if __name__ == '__main__':
    with open('sample_data.txt', 'r') as fileref:
        example = [line[:-1] for line in fileref]

    print('----- part one -----')
    test(True, example, 4512)
    do_it(True, 'day4_data.txt')
    print('----- part two -----')
    test(False, example, 1924)
    do_it(False, 'day4_data.txt')
