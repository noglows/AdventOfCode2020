from pprint import pprint

# Open and read data
directions = open("/Users/jess/Documents/Code/Advent2020/12/Data.txt", "r")
directions = directions.readlines()

east_west = 0
north_south = 0
facing = 90

for inst in directions:
    inst = inst.strip()
    write = int(inst[1:])
    direction = inst[0]
    
    if direction == "N":
        north_south += write
    elif direction == "S":
        north_south -= write
    elif direction == "E":
        east_west += write
    elif direction == "W":
        east_west -= write
    elif direction == "L":
        facing -= write
        if facing < 0:
            facing = facing + 360
    elif direction == "R":
        facing += write
        if facing >= 360: 
            facing = facing - 360
    elif direction == "F":
        if facing == 90:
            east_west += write
        elif facing == 180:
            north_south -= write
        elif facing == 270: 
            east_west -= write
        elif facing == 0:
            north_south += write

print("Part One Solution is: ")
print(abs(east_west) + abs(north_south))
