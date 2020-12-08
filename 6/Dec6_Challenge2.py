# open and read the file
codes = open("/Users/jess/Documents/Code/Advent2020/6/Data.txt", "r")
lines = codes.readlines()

groups = {}
letter_counts = {}
full_line = ""
yes_sum = 0
line_count = 0
team_count = 0

matches = 0

for line in lines:
    if line == "\n":
        line_count += 1
        groups[line_count] = [team_count, full_line.replace('\n', '')]
        full_line = ""
        team_count = 0
    elif line == lines[-1]:
        if full_line == "":
            line_count += 1
            team_count = 1
            groups[line_count] = [team_count, line.replace('\n', '')]
        else:
            line_count += 1
            full_line += line 
            team_count += 1
            groups[line_count] = [team_count, full_line.replace('\n', '')]
    else: 
        full_line += line
        team_count += 1


for i in range(1, line_count+1):
    for item in groups[i][1]:
        if item in letter_counts:
            letter_counts[item] += 1
        else: letter_counts[item] = 1
        if letter_counts[item] == groups[i][0]:
            matches += 1
    letter_counts = {}

print (matches)
    

