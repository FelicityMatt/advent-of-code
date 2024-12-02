def test(function, example: list, answer: int):
    x = function(example)
    print('sample answer is:', x)
    assert x == answer

def do_it(function, file_name):
    with open(file_name, 'r') as fileref:
        lines = [line.strip() for line in fileref]
        return(function(lines))

def part_one_code(lines: list):
    total = 0

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            cur = lines[row][col]
            # check if on edge
            if row == 0 or row == len(lines) - 1 or cur == 0 or cur == len(lines[0]) - 1:
                total += 1

            else:
                # check to the right
                right_visable = True
                for i in range(col + 1, len(lines[0])):
                    if lines[row][i] >= cur:
                        right_visable = False

                # check left 
                left_visable = True
                for j in range(0, col):
                    if lines[row][j] >= cur:
                        left_visable = False

                # check up
                up_visable = True
                for k in range(0, row):
                    if lines[k][col] >= cur:
                        up_visable = False

                # check down
                down_visable = True
                for l in range(row + 1, len(lines)):
                    if lines[l][col] >= cur:
                        down_visable = False

                directions = [right_visable, left_visable, up_visable, down_visable]


                if True in directions:
                    total += 1
            
    return total


def part_two_code(lines: list):
    best_score = 0

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            cur = int(lines[row][col])

            # if it is not an edge tree
            if not (row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines[0]) - 1):
                # print("--- cur:", cur, "---")
                score = 1

                # right, left, up, down
                ranges = [(col + 1, len(lines[0]), 1), (col - 1, -1, -1), (row - 1, -1, -1), (row + 1, len(lines), 1)]

                for i in range(4):
                    # print("--- new direction ---")
                    dis = 0
                    highest_tree = 0

                    for j in range(ranges[i][0], ranges[i][1], ranges[i][2]):
                        # print(j)
                        pos = [(row, j), (row, j), (j, col), (j, col)]
                        new_tree = int(lines[pos[i][0]][pos[i][1]])
                        #print("new tree:", new_tree )
                        # print(lines[pos[i][0]][pos[i][1]])
                        # stop if a tree is the same or higher than the current tree
                        if new_tree >= cur:
                            dis += 1
                            break
                        # else the tree is smaller and can look for another tree
                        else:
                            if new_tree >= highest_tree:
                                dis += 1
                                highest_tree = new_tree
                    # print("dis:", dis)
                    score = score * dis
                    # print("score:", score)
                # print("cur:", cur, "score:", score)

                if score > best_score:
                    best_score = score

    # 120 too low   
    # 2160 too low 
    return best_score


if __name__ == '__main__':
    print()
    with open('day9/day9-sample.txt', 'r') as fileref:
        example = [line.strip() for line in fileref]

    filename = 'day9/day9-data.txt'
    answer_one = 21
    answer_two = 8

    print('----- part one -----')
    test(part_one_code, example, answer_one)
    print("the answer to part one is", do_it(part_one_code, filename))
    print('----- part two -----')
    test(part_two_code, example, answer_two)
    print("the answer to part one is", do_it(part_two_code, filename))
    print()
