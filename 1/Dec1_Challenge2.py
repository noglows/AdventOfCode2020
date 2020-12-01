codes = open("/Users/jess/Documents/Code/Advent2020/1/Data.txt", "r")
lines = codes.readlines()
lines = [int(i) for i in lines]

def find2020():
    for x in lines:
        for y in lines: 
            for z in lines:
                if x + y + z == 2020:
                    return(x * y * z)
            

print(find2020())
