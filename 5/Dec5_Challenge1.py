import math
ticket_file = open("/Users/jess/Documents/Code/Advent2020/5/Data.txt", "r")
tickets = ticket_file.readlines()
max_code = 0


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

print(max_code)