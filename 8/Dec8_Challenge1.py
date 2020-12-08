# open and read the file
instructions = open("/Users/jess/Documents/Code/Advent2020/8/SampleData.txt", "r")
instructions = instructions.readlines()


# line_log = {}
# line_count = 0
# accumulator = 0
# stillMove = True

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
line_count = len(instructions)

# find the possible spots
i = 0
places = []
for instruction in instructions:
    instruction = instruction.split(" ")
    if instruction[0] == "nop" or instruction[0] == "jmp":
        places.append(i)
    i += 1
        

def find_the_fix(to_test):

    line_log = {}
    line_count = 0
    accumulator = 0
    stillMove = True
    while stillMove == True: 
        if line_count in line_log:
            stillMove = False 
        else:
            line_log[line_count] = 1
            try:
                instruction = to_test[line_count].split(" ")
                if instruction[0] == "nop":
                    line_count += 1
                elif instruction[0] == "acc":
                    sign = instruction[1][0]
                    value = instruction[1].replace('\n', "")            
                    value = abs(int(value))
                    if sign == "+":
                        accumulator = accumulator + value
                    elif sign == "-": 
                        accumulator = accumulator - value
                    line_count += 1
                elif instruction[0] == "jmp":
                    sign = instruction[1][0]
                    value = instruction[1].replace('\n', "")
                    value = abs(int(value))
                    if sign == "+":
                        line_count = line_count + value
                    elif sign == "-": 
                        line_count = line_count - value
            except IndexError:
                break
    print("len is: ")
    print(len(line_log.keys()))
    print("line count is: ")
    print(line_count)
    print(len(line_log.keys()) == line_count)
    if len(line_log.keys()) == line_count:
        print("found it here:")
        print("it's this one")
        print(accumulator)
        return accumulator
    else:
        print(accumulator) 
        return "Not this one"


for place in places: 
    print("the place is: ")
    print(place)
    instructions_new = instructions[:]
    if instructions[place].split(" ")[0] == "nop":
        instructions_new[place] = instructions_new[place].replace("nop", "jmp")
    elif instructions[place].split(" ")[0] == "jmp":
        instructions_new[place] = instructions_new[place].replace("jmp", "nop")
    a = find_the_fix(instructions_new)
    print(a)

