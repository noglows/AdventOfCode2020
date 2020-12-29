# Imports
import math
import sys


# Open and read the data
ticket_file = open("/Users/jess/Documents/Code/Advent2020/5/Data.txt", "r")
tickets = ticket_file.readlines()
max_code = 0

# Part One: 
def find_row(ticket):
    top = 127
    bottom = 0
    for i in range(7):
        if ticket[i] == "F":
            top = math.floor(top - ((top - bottom)/2))
        elif ticket[i] == "B":
            bottom = math.floor(bottom + ((top - bottom)/2))
        i += 1
    if ticket[7] == "F":
        row = bottom
    else: row = top
    return row

def find_seat(ticket):
    right = 7
    left = 0
    for i in range(7, 9):
        if ticket[i] == "L":
            right = math.floor(right - ((right - left)/2))
        elif ticket[i] == "R":
            left = math.ceil(left + ((right - left)/2))
        i += 1
    if tickets[0][7] == "L":
        col = left
    else: col = right
    return col

def seat_code(ticket):
    row = find_row(ticket)
    col = find_seat(ticket)
    return ((row * 8) + col)

for ticket in tickets:
    code = seat_code(ticket)
    if code > max_code:
        max_code = code

print("Part One Solution is: ")
print(max_code)


# Part Two
seen = set()
missing = []
highest = 0
lowest = sys.maxsize

for ticket in tickets:
    min_row, max_row, min_col, max_col = 0, 127, 0, 7
    last_row_dir, last_col_dir = None, None

    for char in ticket:
      if char == "F" or char == "B":
        last_row_dir = char
        if char == "F":
          max_row = max_row - round((max_row - min_row) / 2)
        else:
          min_row = min_row + round((max_row - min_row) / 2)
      elif char == "L" or char == "R":
        last_col_dir = char
        if char == "L":
          max_col = max_col - round((max_col - min_col) / 2)
        else:
          min_col = min_col + round((max_col - min_col) / 2)

    row = min_row if last_row_dir == "F" else max_row
    col = min_col if last_col_dir == "L" else max_col
    code = row * 8 + col
    seen.add(code)
    if code > highest:
        highest = code
    if code < lowest:
        lowest = code

for code in range(lowest, highest):
    if code not in seen:
        missing.append(code)

print("Part Two Solution is: ")
print(missing[0])


