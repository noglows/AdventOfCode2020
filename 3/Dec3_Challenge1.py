# open and read the file
codes = open("/Users/jess/Documents/Code/Advent2020/3/Data.txt", "r")
lines = codes.readlines()

row_pointer = 0
vertical_pointer = 0
tree_count = 0

def move(starting_row, starting_column):
    starting_row = starting_row + 1
    starting_column = starting_column + 3
    starting_column = starting_column % 31

    return ([starting_row, starting_column])

def checkForTree(tree_count):
    if lines[row_pointer][vertical_pointer] == "#":
        tree_count += 1
    return tree_count


for line in lines:
    new_places = move(row_pointer, vertical_pointer)
    tree_count = checkForTree(tree_count)
    row_pointer = new_places[0]
    vertical_pointer = new_places[1]
print(tree_count)


        