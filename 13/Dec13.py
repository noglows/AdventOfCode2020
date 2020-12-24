
# Open and read data
bus = open("/Users/jess/Documents/Code/Advent2020/13/Data.txt", "r")
bus = bus.readlines()

start = int(bus[0])
options = bus[1]
options = options.split(",")
new_options = []

for option in options:
    if option != "x":
        new_options.append(int(option))

potentials = {} 

for option in new_options:
    target = start % option 
    value = option - target 
    goal = start + value 

    potentials[goal] = option 

time = min(potentials.keys())
bus_id = potentials[time]

answer = (time - start) * bus_id
print("Part One Solution is: ")
print(answer)
