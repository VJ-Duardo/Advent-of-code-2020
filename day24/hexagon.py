import re

tiles = []
with open("tiles.txt") as file:
    tiles = [re.findall("ne|se|sw|nw|w|e", line) for line in file.read().splitlines()]

directions = {'ne': (0.5, 1), 'e': (1, 0), 'se': (0.5, -1),
              'sw': (-0.5, -1), 'w': (-1, 0), 'nw': (-0.5, 1)}

WHITE = True
BLACK = False


def get_flipped_tiles():
    tile_map = {}
    for tile in tiles:
        x, y = 0, 0
        for direc in tile:
            x += directions[direc][0]
            y += directions[direc][1]
        if (x, y) not in tile_map:
            tile_map[(x, y)] = BLACK
        else:
            tile_map[(x, y)]^= True

    return tile_map


def art_exhibit(tile_map, days):
    for i in range(days):
        for tile in list(tile_map.keys()):
            for direcs in list(directions.values()):
                if (tile[0]+direcs[0], tile[1]+direcs[1]) not in tile_map:
                    tile_map[(tile[0]+direcs[0], tile[1]+direcs[1])] = WHITE
        new_tile_map = tile_map.copy()
        for tile in list(tile_map.keys()):
            adjacent = get_adjacent_black_count(tile_map, *tile)
            if tile_map[tile] == BLACK and (adjacent == 0 or adjacent > 2):
                new_tile_map[tile] = WHITE
            elif tile_map[tile] == WHITE and adjacent == 2:
                new_tile_map[tile] = BLACK
        tile_map = new_tile_map
        
    return tile_map
        

def get_adjacent_black_count(tile_map, x, y):
    c = 0
    for direcs in list(directions.values()):
        if (x+direcs[0], y+direcs[1]) in tile_map and tile_map[(x+direcs[0], y+direcs[1])] == BLACK:
            c += 1
    return c
        


tile_map = get_flipped_tiles()
print(list(tile_map.values()).count(BLACK))

print(list(art_exhibit(tile_map, 100).values()).count(BLACK))


        


