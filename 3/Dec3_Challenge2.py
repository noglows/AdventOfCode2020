# open and read the file
codes = open("/Users/jess/Documents/Code/Advent2020/3/Data.txt", "r")
lines = codes.readlines()
length = len(lines)
col_count = len(lines[0])-1

def move(starting_row, starting_column, right_shift, down_shift):
    starting_row = starting_row + down_shift
    starting_column = starting_column + right_shift
    starting_column = starting_column % col_count
    return ([starting_row, starting_column])

def checkForTree(rp, vp, tree_count):
    if rp <= length:
        if lines[rp][vp] == "#":
            tree_count += 1
    return tree_count

def skiPath(lines, right_shift, down_shift):
    row_pointer = 0
    vertical_pointer = 0
    tree_count = 0
    for line in lines:
        new_places = move(row_pointer, vertical_pointer, right_shift, down_shift)
        tree_count = checkForTree(row_pointer, vertical_pointer, tree_count)
        row_pointer = new_places[0]
        vertical_pointer = new_places[1]
    return tree_count


one_one_path = skiPath(lines, 1, 1)
print(one_one_path)
three_one_path = skiPath(lines, 3, 1)
print(three_one_path)
five_one_path = skiPath(lines, 5, 1)
print(five_one_path)
seven_one_path = skiPath(lines, 7, 1)
print(seven_one_path)
one_two_path = skiPath(lines, 1, 2)
print(one_two_path)

answer = one_one_path * three_one_path * five_one_path * seven_one_path * one_two_path
print(answer)


        