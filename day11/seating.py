FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
TOLERANCE = 5

init_seats = []
with open("seats.txt") as file:
    init_seats = list(map(list, file.read().splitlines()))


def get_adjacent_count(seats, i, j):
    c = 0
    for k in [(i, j-1), (i, j+1), (i-1, j), (i+1, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
        if 0 <= k[0] < len(seats) and 0 <= k[1] < len(seats[i]) and seats[k[0]][k[1]] == OCCUPIED:
            c += 1
    return c


def get_real_adjacent_count(seats, i, j):
    c = 0
    for k in [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        l = i+k[0]
        m = j+k[1]
        while 0 <= l < len(seats) and 0 <= m < len(seats[l]):
            if seats[l][m] != FLOOR:
                if seats[l][m] == OCCUPIED:
                    c += 1
                break
            l += k[0]
            m += k[1]
    return c
                

    
def update_seats(seats):
    new_seats = []
    for i in range(0, len(seats)):
        line = seats[i].copy()
        for j in range(0, len(seats[i])):
            seat = line[j]
            if seat == EMPTY and get_real_adjacent_count(seats, i, j) == 0:
                line[j] = OCCUPIED
            elif seat == OCCUPIED and get_real_adjacent_count(seats, i, j) >= TOLERANCE:
                line[j] = EMPTY
        new_seats.append(line)
    return new_seats


def get_final_seat_count():
    seats = update_seats(init_seats)
    old_count = 0
    current_count = sum(seats, []).count(OCCUPIED)
    while old_count != current_count:
        old_count = current_count
        seats = update_seats(seats)
        current_count = sum(seats, []).count(OCCUPIED)
    return current_count


print(get_final_seat_count())
