# open and read the file
adapters = open("/Users/jess/Documents/Code/Advent2020/10/Data.txt", "r")
adapters = adapters.readlines()

adapter_list = [0]
one_jolt = 0
two_jolt = 0
three_jolt = 1

for adapter in adapters:
    adapter = adapter.replace("\n", "")
    adapter = int(adapter)
    adapter_list.append(adapter)

adapter_list.sort()


# Part One

for i in range(1, len(adapter_list)):
    if adapter_list[i] - 1 == adapter_list[i-1]:
        one_jolt += 1
    elif adapter_list[i] - 2 == adapter_list[i-1]:
        two_jolt += 1
    elif adapter_list[i] - 3 == adapter_list[i-1]:
        three_jolt += 1
    else:
        print("something is wrong")


solution = one_jolt * three_jolt
print ("The Part One Solution Is: ")
print (solution)


# Part Two
max_adapter = adapter_list[-1] + 3