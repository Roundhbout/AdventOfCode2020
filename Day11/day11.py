import pprint
import time
import copy

from collections import defaultdict
f = open("input.txt", "r")

file = f.read().split()

seats = list(map(lambda row: [char for char in row], file))

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

"""
- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.

Use intermediate adjacency (include diagonals)
"""

# return all inbounds neighbors of the seat at row, col
def get_neighbors(row, col, seats):
    neighbors = []
    #print(f"FOR CELL {row}, {col}")
    for r in range(max(0, row - 1), min(len(seats), row + 2)):
        for c in range(max(0, col - 1), min(len(seats[row]), col + 2)):
            #print(r, c)
            if not(r == row and c == col):
                
                neighbors.append(seats[r][c])
    return neighbors

assert(len(get_neighbors(1, 1, [[1, 1, 1],[2, 2, 2],[3, 3, 3]])) == 8)

"""
def manhattan_dist(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return abs(y2 - y1) + abs(x2 - x1)

# determine the location of (r, c) in reference to (refrow, refcol)
def get_direction(refrow, refcol, r, c):
    # i hate this
    answer_key = {
        (False, True, False, False) : "n",
        (False, True, True, False) : "ne",
        (False, False, True, False) : "e",
        (True, False, True, False) : "se",
        (True, False, False, False) : "s",
        (True, False, False, True) : "sw",
        (False, False, False, True) : "w",
        (False, True, False, True) : "nw",
    }
    r_greater = r > refrow
    r_less = r < refrow
    c_greater = c > refcol
    c_less = c < refcol
    #r_equal = r == refrow
    #c_equal = c ==refcol
    try:
        return answer_key[(r_greater, r_less, c_greater, c_less)]
    except:
        print(refrow, refcol, r, c)


def along_visible_line(row, col, r, c):
    diag = (abs(row - r) == abs(col - c) != 0)
    vert = (abs(row - r) != abs(col - c) == 0)
    hori = (abs(col - c) != abs(row - r) == 0)
    return diag or vert or hori
"""
def get_first_visible_neighbors(row, col, seats):
    num_rows = len(seats)
    num_cols = len(seats[0])
    directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
    visible_neighbors = []


    for offset_row in range(-1, 2):
        for offset_col in range(-1, 2):
            r = row + offset_row
            c = col + offset_col
            if (offset_row == offset_col == 0 or
                row >= num_rows or r < 0 or
                col >= num_cols or c < 0):
                continue
            while True:
                tile = seats[row][col]
                if tile != FLOOR:
                    visible_neighbors.append(tile)
                if (tile != FLOOR or
                    r + offset_row >= num_rows or r + offset_row < 0 or
                    c + offset_col > num_cols or r + offset_col < 0):
                    break
                r += offset_row
                c += offset_col
    """
    #print(f"FOR {row},{col}----------------------")
    # need to view seats along cardinal and intermediate lines from rowcol, starting inwards out
    visible_lines = [(r, c) for r in range(len(seats)) for c in range(len(seats[r])) if along_visible_line(row, col, r, c)]
    # sort visible lines to have nearest cells first
    visible_lines.sort(key=lambda rc : manhattan_dist(rc, (row, col)))

    for rowcol in visible_lines:
        r, c = rowcol
        #print(rowcol)
        # get the direction that (r,c) is from (row, col)

        dir = get_direction(row, col, r, c)
        # if we haven't already seen an earlier seat in that direction and the current seat isn't a floor
        if dir in directions and seats[r][c] != FLOOR:
            visible_neighbors.append(seats[r][c])
            directions.remove(dir)
        
        #terminate early if we've found every direction
        if not directions:
            break
    
    """
    #print(row, col)
    #print(visible_neighbors)
    return visible_neighbors



def update_seats(seats, empties, occupancies):
    for row, col in empties:
        seats[row][col] = EMPTY
    for row, col in occupancies:
        seats[row][col] = OCCUPIED
    return seats

"""
seats -> list of list of chars : 2d grid of the seat layout
occupied_count -> int : number of occupieds in neighbors before an occupied seat becomes an empty
neighbor_type -> boolean: determine which means of detecting neighbors to use (TRUE IF IMMEDIATE NEIGHBORS)
"""
def simulate_seating_changes(seats, occupied_count, neighbor_type):

    changes = 1

    # run the simulation until the layout doesn't change
    while changes:
        changes = 0
        start_time = time.time()
    
        new_seats = copy.deepcopy(seats)
        # loop through each seat
        for row in range(len(seats)):
            for col in range(len(seats[row])):
                # get the seat's status
                cur_seat = seats[row][col]
                # get the seat's neighbors
                if cur_seat != FLOOR:
                    if neighbor_type:
                        cur_neighbors = get_neighbors(row, col, seats)
                    else:
                        cur_neighbors = get_first_visible_neighbors(row, col, seats)
                    # if the seat is empty, determine if none of it's neighbors are occupied
                    if cur_seat == EMPTY:
                        if OCCUPIED not in cur_neighbors:
                            # add this seat to the new occupancy list, we'll update in batch later
                            new_seats[row][col] = OCCUPIED
                            changes += 1
                    # if the seat is occupied, determine if there are at least four occupancies around it
                    elif cur_seat == OCCUPIED:
                        if cur_neighbors.count(OCCUPIED) >= occupied_count:
                            # add this seat to the new empty list, we'll update in batch later
                            new_seats[row][col] = EMPTY
                            changes += 1
        
        # i could check here to see if there are any changes
        #print(len(new_occupancies), len(new_empties))
        seats = new_seats
        #print(f"{time.time() - start_time} SECONDS")
        
    return seats


p1answer = sum([row.count(OCCUPIED) for row in simulate_seating_changes(seats, 4, True)])
print(f"PART 1: {p1answer}")

p2answer = sum([row.count(OCCUPIED) for row in simulate_seating_changes(seats, 5, False)])
print(f"PART 2: {p2answer}")