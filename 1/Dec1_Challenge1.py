

codes = open("/Users/jess/Documents/Code/Advent2020/1/Data.txt", "r")
lines = codes.readlines()

log = {}

for line in lines:
    line = int(line)
    if line in log:
        print("found it")
        print(log[line] * line)
    else:
        looking_value = 2020 - line 
        log[looking_value] = line

