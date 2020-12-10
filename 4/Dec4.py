passports = open("/Users/jess/Documents/Code/Advent2020/4/Data.txt", "r")
lines = passports.readlines()

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
            
print("Part One Solution is: ")
print(valid)
        

# Part Two 

passport = ""
valid = 0

def validate_byr(birth_year):
    if len(birth_year) == 4:
        birth_year = int(birth_year)
        if birth_year >= 1920 and birth_year <= 2002:
            return True
        else:
            return False
    else: 
        return False

def validate_iyr(issue_year):
    if len(issue_year) == 4:
        issue_year = int(issue_year)
        if issue_year >= 2010 and issue_year <= 2020:
            return True
        else:
            return False
    else: 
        return False

def validate_eyr(expire_year):
    if len(expire_year) == 4:
        expire_year = int(expire_year)
        if expire_year >= 2020 and expire_year <= 2030:
            return True
        else:
            return False
    else: 
        return False

def validate_hgt(height):
    if height.count("cm") > 0:
        height = int(height.replace("cm", ""))
        if height >= 150 and height <= 193:
            return True
        else:
            return False
    elif height.count("in") > 0:
        height = int(height.replace("in", ""))
        if height >= 59 and height <= 76:
            return True
        else:
            return False
    else: return False 


def validate_hcl(hair_color):
    allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    if len(hair_color) == 7:
        if hair_color[0] == "#":
            hair_color = hair_color.replace("#", "")
            for letter in hair_color:
                if letter not in allowed: 
                    return False
                return True
            else: return False
        else: return False
    else: return False

def validate_ecl(eye_color):
    acceptable = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if eye_color in acceptable:
        return True
    else: return False

def validate_pid(passport_id):
    if len(passport_id) == 9:
        if passport_id.isnumeric:
            return True 
        else: return False
    else: return False


def check_validity(passport):
    pass_dict = {}
    for value in passport: 
        item = value.split(":")
        pass_dict[item[0]] = item[1].rstrip()
    byr = validate_byr(pass_dict["byr"])
    ecl = validate_ecl(pass_dict["ecl"])
    eyr = validate_eyr(pass_dict["eyr"])
    hcl = validate_hcl(pass_dict["hcl"])
    hgt = validate_hgt(pass_dict["hgt"])
    iyr = validate_iyr(pass_dict["iyr"])
    pid = validate_pid(pass_dict["pid"])

    isValid = byr and ecl and eyr and hcl and hgt and iyr and pid
    return isValid

for passport in passports:
    split = passport.split(" ")
    split.pop(-1)
    if len(split) == 8:
        if check_validity(split):
            valid += 1
    elif len(split) == 7:
        valid_count = 0
        for a in split:
            valid_count += a.count("cid")
        if valid_count == 0:
            if check_validity(split):
                valid += 1

print("Part Two Solution is: ")          
print(valid)
        