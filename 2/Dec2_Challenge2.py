# Open and read the file
passwords = open("/Users/jess/Documents/Code/Advent2020/2/Data.txt", "r")
lines = passwords.readlines()

# Part 1
legal = 0

for line in lines:
    # Split the line into parts
    line_items = line.split(" ")

    # Define a variable for each part of the line
    string_range = line_items[0].split("-")
    target = line_items[1][0]
    password = line_items[2]
    letter_count = password.count(target)

    # Convert string values to range
    int_range = range(int(string_range[0]), int(string_range[1])+1)

    # Count the legal passwords
    if letter_count in int_range:
        legal += 1

print("Part One Solution is: ")
print(legal)

# Part Two
legal = 0

for line in lines:
    # Split the line into parts
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
    if not(in_spot_one and in_spot_two) and (in_spot_one or in_spot_two):
        legal +=1

print("Part Two Solution is: ")
print(legal)


