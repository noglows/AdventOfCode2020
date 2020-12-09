# open and read the file
transmissions = open("/Users/jess/Documents/Code/Advent2020/9/Data.txt", "r")
transmissions = transmissions.readlines()


preamble = 25
i = 0
preamble_values = []
invalid_num = 0

def find_sum_pairs(value_list, sum_value):
    sum_value = int(sum_value) 
    array = [i+j for i in value_list for j in value_list]
    return (sum_value in array)


for transmission in transmissions:
    if i < preamble:
        transmission = transmission.replace("\n", "")
        transmission = int(transmission)
        preamble_values.append(transmission)
        i += 1
    elif i == (len(transmissions)-1):
        break
    elif i >= preamble:
        is_sum = find_sum_pairs(preamble_values, transmission)
        if is_sum is False:
            invalid_num = transmission
            print(transmission)
        preamble_values.pop(0)
        transmission = transmission.replace("\n", "")
        transmission = int(transmission)
        preamble_values.append(transmission)
        i += 1



