import math
import sys

ticket_file = open("/Users/jess/Documents/Code/Advent2020/5/Data.txt", "r")
tickets = ticket_file.readlines()

def seat_code(ticket):
    row = find_row(ticket)
    col = find_seat(ticket)
    print(row)
    print(col)
    return ((row * 8) + col)


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

print(missing)


