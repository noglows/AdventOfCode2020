from pprint import pprint

# open and read the file
instructions = open("/Users/jess/Documents/Code/Advent2020/8/Data.txt", "r")
instructions = instructions.readlines()

i = 0
places = []

new_instructions = []
all_instructions = []

for instruction in instructions:
    instruction = instruction.replace('\n', "")
    instruction = instruction.split(" ")
    if instruction[0] == "nop" or instruction[0] == "jmp":
        places.append(i)
    i += 1
    new_instructions.append([instruction[0], instruction[1]])

all_instructions.append(new_instructions)

for place in places:
    test_case = []
    i = 0
    for item in new_instructions:
        if i == place:
            if item[0] == "jmp":
                test_case.append(["nop", item[1]])
            elif item[0] == "nop":
                test_case.append(["jmp", item[1]])
        else: test_case.append(item)
        i += 1
    all_instructions.append(test_case)

line_log = {}
line_count = 0
accumulator = 0
stillMove = True

def test_the_input(test_case):
    line_log = {}
    line_count = 0
    accumulator = 0
    stillMove = True
    
    while stillMove == True: 
        if line_count in line_log:
            stillMove = False 
        elif line_count >= len(instructions):
            stillMove = False
            return accumulator
        else:
            line_log[line_count] = 1
            if test_case[line_count][0] == "nop":
                line_count += 1
            elif test_case[line_count][0] == "acc":
                sign = test_case[line_count][1][0]
                value = test_case[line_count][1]
                value = abs(int(value))
                if sign == "+":
                    accumulator = accumulator + value
                elif sign == "-": 
                    accumulator = accumulator - value
                line_count += 1
            elif test_case[line_count][0] == "jmp":
                sign = test_case[line_count][1][0]
                value = test_case[line_count][1]
                value = abs(int(value))
                if sign == "+":
                    line_count = line_count + value
                elif sign == "-": 
                    line_count = line_count - value

    if len(line_log.keys()) == len(instructions):
        return accumulator
    else: 
        return
        
for test in all_instructions:
    a = test_the_input(test)
    if a is not None:
        print(a)