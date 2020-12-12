from math import sin, cos, pi

TURN_STEP = 90
DIRECS = 4

instructions = []
with open("directions.txt") as file:
    instructions = [(entry[:1], int(entry[1:])) for entry in file.read().splitlines()]

init_ship = {'x': 0, 'y': 0, 'heading': 1}
init_waypoint = {'x_off': 10, 'y_off': 1}


def do_instructions(ship):
    for instruction in instructions:
        instr, val = instruction[0], instruction[1]
        if instr in ['L', 'R']:
            change = int(val/TURN_STEP)
            ship['heading'] += change if instr == 'R' else -change
        elif instr in ['N', 'E', 'S', 'W']:
            if instr in ['N', 'S']:
                ship['y'] += val if instr == 'N' else -val
            else:
                ship['x'] += val if instr == 'E' else -val
        elif instr == 'F':
            if ship['heading'] % DIRECS in [0, 2]:
                ship['y'] += val if ship['heading'] % DIRECS == 0 else -val
            else:
                ship['x'] += val if ship['heading'] % DIRECS == 1 else -val
    return abs(ship['x'])+abs(ship['y'])



def do_real_instructions(ship, waypoint):
    for instruction in instructions:
        instr, val = instruction[0], instruction[1]
        if instr in ['L', 'R']:
            rad = val*pi/180 if instr == 'L' else (-val)*pi/180
            x, y = waypoint['x_off'], waypoint['y_off']
            waypoint['x_off'] = round(x*cos(rad)-y*sin(rad))
            waypoint['y_off'] = round(y*cos(rad)+x*sin(rad))
        elif instr in ['N', 'E', 'S', 'W']:
            if instr in ['N', 'S']:
                waypoint['y_off'] += val if instr == 'N' else -val
            else:
                waypoint['x_off'] += val if instr == 'E' else -val
        elif instr == 'F':
            ship['x'] += val*waypoint['x_off']
            ship['y'] += val*waypoint['y_off']
    return abs(ship['x'])+abs(ship['y'])



print(do_instructions(init_ship.copy()))
print(do_real_instructions(init_ship, init_waypoint))
