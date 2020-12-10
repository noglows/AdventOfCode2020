# Open and read file
codes = open("/Users/jess/Documents/Code/Advent2020/1/Data.txt", "r")
lines = codes.readlines()

# Part 1
log = {}

for line in lines:
    line = int(line)
    if line in log:
        print("Part One Solution is: ")
        print(log[line] * line)
    else:
        looking_value = 2020 - line 
        log[looking_value] = line


# Part 2
lines = [int(i) for i in lines]

def find2020():
    for x in lines:
        for y in lines: 
            for z in lines:
                if x + y + z == 2020:
                    return(x * y * z)
            
print("Part Two Solution is: ")
print(find2020())

