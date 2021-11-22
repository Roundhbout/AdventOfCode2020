import math

f = open("input.txt", "r")

seats = list(map(lambda x: x[:-1] , f.readlines()))

def get_row_seat_num(seat):
    direction_map = {"F" : True, "B" : False, "L" : True, "R" : False}
    forwardbackwards = seat[:-3]
    leftright = seat[-3:]
    low = 0
    high = 127
    left = 0
    right = 7
    for char in forwardbackwards:
        mid = (low + (high - 1)) // 2
        if direction_map[char]:
            high = mid
        else:
            low = mid + 1
    row = low

    for char in leftright:
        mid = (left + (right - 1)) // 2
        if direction_map[char]:
            right = mid
        else:
            left = mid + 1

    seat_num = left
    return (row, seat_num)

max_id = float('-inf')
seat_ids = []
for seat in seats:
    row, seat_num = get_row_seat_num(seat)
    cur_id = (row * 8) + seat_num
    max_id = max(cur_id, max_id)
    seat_ids.append(cur_id)

print(f"HIGHEST ID: {max_id}")

"""

s = set()
for seat in seat_ids:
    if seat - 2 in s:
        print(f"MY SEAT: {seat - 1}")
    s.add(seat)
"""
    
    
