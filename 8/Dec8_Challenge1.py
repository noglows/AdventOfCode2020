# open and read the file
instructions = open("/Users/jess/Documents/Code/Advent2020/8/Data.txt", "r")
instructions = instructions.readlines()


line_log = {}
line_count = 0
accumulator = 0
stillMove = True

while stillMove == True: 
    if line_count in line_log:
        stillMove = False 
    else:
        line_log[line_count] = 1
        instruction = instructions[line_count].split(" ")
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


print (accumulator)


