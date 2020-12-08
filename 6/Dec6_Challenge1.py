# open and read the file
codes = open("/Users/jess/Documents/Code/Advent2020/6/Data.txt", "r")
lines = codes.readlines()

groups = []
full_line = ""
yes_sum = 0
line_count = 0

for line in lines:
    if line == "\n":
        groups.append(full_line.replace('\n', ''))
        full_line = ""
    elif line == lines[-1]:
        if full_line == "":
            groups.append(line.replace('\n', ''))
        else:
            full_line += line 
            groups.append(full_line.replace('\n', ''))
    else: full_line += line


for group in groups:
    count = len(set(group))
    yes_sum += count

print (yes_sum)