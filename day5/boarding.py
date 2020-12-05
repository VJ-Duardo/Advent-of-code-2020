FRONT = 'F'
MAX_ROW = 127
ROW_SIZE = 8

LEFT = 'L'
MAX_COLUMN = 7

passes = [] 
with open("passes.txt", "r") as file:
    passes = file.read().splitlines()


def get_position(seat_input, max_pos):
    seats = list(range(0,max_pos+1))
    for i in range(0, len(seat_input)):
        if seat_input[i] == FRONT or seat_input[i] == LEFT:
            seats = seats[:int(len(seats)/2)]
        else:
            seats = seats[int(len(seats)/2):]
            
    return int(seats[0])
        

def get_seat_id(seat_code):
    return get_position(seat_code[:7], MAX_ROW) * ROW_SIZE + get_position(seat_code[-3:], MAX_COLUMN)


def get_highest_seat_id():
    return max(list(map(lambda a_pass: get_seat_id(a_pass), passes)))


def get_missing_id():
    all_given_ids = list(map(lambda a_pass: get_seat_id(a_pass), passes))
    all_ids = list(range(0, get_highest_seat_id()))
    missing_ids = sorted(set(all_ids) - set(all_given_ids))
    return list(filter(lambda sid: (sid[0]-1 < 0 or (sid[0]-1 > 0 and int(missing_ids[sid[0]-1]) != sid[1]-1))
                       and (sid[0]+1 > len(missing_ids)-1 or (sid[0]+1 <= len(missing_ids)-1 and int(missing_ids[sid[0]+1]) != sid[1]+1)), enumerate(missing_ids)))[0][1]

print(get_highest_seat_id())
print(get_missing_id())
