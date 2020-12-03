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

    # identify the two possible positions and account for index 0
    spot_one = int(string_range[0])-1
    spot_two = int(string_range[1])-1

    # count the legal passwords
    in_spot_one = password[spot_one] == target
    in_spot_two = password[spot_two] == target
    if in_spot_one and in_spot_two:
        print("not here")
    elif in_spot_one or in_spot_two:
        legal +=1
    else:
        print("not here")
        
print(legal)


