
# Open and read data
numbers = open("/Users/jess/Documents/Code/Advent2020/15/Data.txt", "r")
numbers = numbers.readlines()

# Part One
game_input = []
spoken = []

track = {}

game = numbers[0].split(",")
numbers_length = len(game_input)

turn = 0
for item in game:
    spoken.append(int(item))
    track[int(item)] = turn
    turn += 1

count = numbers_length + 1
iterator = 5
count = iterator + 1

while count < 2020:
    look = spoken[iterator]
    if look in track:
        spoken.append(iterator - track[look])
    else:
        spoken.append(0)
    track[look] = iterator
    iterator +=1 
    count += 1

print("Part One Solution is: ")
print(spoken[-1])

game_input = []
spoken = []

track = {}

game = numbers[0].split(",")
numbers_length = len(game_input)

turn = 0
for item in game:
    spoken.append(int(item))
    track[int(item)] = turn
    turn += 1

count = numbers_length + 1
iterator = 5
count = iterator + 1

while count < 30000000:
    look = spoken[iterator]
    if look in track:
        spoken.append(iterator - track[look])
    else:
        spoken.append(0)
    track[look] = iterator
    iterator +=1 
    count += 1

print("Part Two Solution is: ")
print(spoken[-1])