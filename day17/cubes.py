import copy

ACTIVE = '#'
INACTIVE = '.'
DIMENSIONS = 4

space = []
with open("initial.txt") as file:
    space = [[[list(x) for x in file.read().splitlines()]]]

neighbours = []
def neighbour_combinations(c, curr):
    if c == 0:
        return neighbours.append(curr)
    for i in [-1, 1, 0]:
        neighbour_combinations(c-1, curr+[i])
neighbour_combinations(DIMENSIONS, [])
neighbours.remove([0, 0, 0, 0])
    

def check_position(active, x, y, z, w):
    active_neighbours = 0
    for n in neighbours:
        if 0 <= x+n[0] < len(space[w][z][y]) and 0 <= y+n[1] < len(space[w][z]) and 0 <= z+n[2] < len(space[w]) and 0 <= w+n[3] < len(space):
            if space[w+n[3]][z+n[2]][y+n[1]][x+n[0]] == ACTIVE:
                active_neighbours += 1

    return (active and active_neighbours in [2, 3]) or (not active and active_neighbours == 3)
    
    

def do_cycle():
    global space
    space.insert(0, [[['.' for i in range(len(space[0][0][0]))] for j in range(len(space[0][0]))] for k in range(len(space[0]))])
    space.append([[['.' for i in range(len(space[0][0][0]))] for j in range(len(space[0][0]))] for k in range(len(space[0]))])
    for w in range(len(space)):
        space[w].insert(0, [['.' for i in range(len(space[w][0][0]))] for j in range(len(space[w][0]))])
        space[w].append([['.' for i in range(len(space[w][0][0]))] for j in range(len(space[w][0]))])
        for z in range(len(space[w])):
            space[w][z].insert(0, ['.' for i in range(len(space[w][z][0]))])
            space[w][z].append(['.' for i in range(len(space[w][z][0]))])
            for y in range(len(space[w][z])):
                space[w][z][y].insert(0, '.')
                space[w][z][y].append('.')

    new_space = copy.deepcopy(space)
    for w in range(len(space)):
        for z in range(len(space[w])):
            for y in range(len(space[w][z])):
                for x in range(len(space[w][z][y])):
                    if check_position(space[w][z][y][x] == ACTIVE, x, y, z, w):
                        new_space[w][z][y][x] = ACTIVE
                    else:
                        new_space[w][z][y][x] = INACTIVE
    space = new_space


def get_cubes_after_cycles(amount):
    for i in range(amount):
        do_cycle()
    return sum(sum([sum(y, []) for y in space], []), []).count(ACTIVE)

print(get_cubes_after_cycles(6))
