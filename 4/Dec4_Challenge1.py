codes = open("/Users/jess/Documents/Code/Advent2020/4/Data.txt", "r")
lines = codes.readlines()

passports = []
passport = ""
valid = 0

for line in lines:
    if line == "\n" or line == lines[-1]:
        passports.append(passport)
        passport = "" 
    else:
        passport += line
        passport += " "
    

for passport in passports:
    split = passport.split(" ")
    split.pop(-1)
    if len(split) == 8:
        valid += 1
    elif len(split) == 7:
        valid_count = 0
        for a in split:
            valid_count += a.count("cid")
        if valid_count == 0:
            valid += 1
            


print(valid)
        