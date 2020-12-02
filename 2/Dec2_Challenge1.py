# open and read the file
codes = open("/Users/jess/Documents/Code/Advent2020/2/Data.txt", "r")
lines = codes.readlines()

legal = 0

for line in lines:
    # split the line into parts
    line_items = line.split(" ")

    # define a variable for each part of the line
    string_range = line_items[0].split("-")
    target = line_items[1][0]
    password = line_items[2]
    letter_count = password.count(target)


    # convert string values to range
    int_range = range(int(string_range[0]), int(string_range[1])+1)

    # count the legal passwords
    if letter_count in int_range:
        legal += 1

print(legal)


