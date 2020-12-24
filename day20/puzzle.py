import re


DRAGON_SIZE = 15

class Tile:
    def __init__(self, number, lines):
        self.number = number
        self.top = lines[0]
        self.bottom = lines[len(lines)-1]
        self.left = ''.join([l[0] for l in lines])
        self.right = ''.join([l[-1:] for l in lines])
        self.all = lines

        self.prev = None
        self.next = None
        self.above = None
        self.below = None

    def rotate(self):
        self.top, self.left, self.bottom, self.right = self.left[::-1], self.bottom, self.right[::-1], self.top
        self.all = rotate_list(self.all)       

    def vert_flip(self):
        self.top, self.bottom, self.left, self.right = self.bottom, self.top, self.left[::-1], self.right[::-1]
        self.all = self.all[::-1]

    def hor_flip(self):
        self.left, self.right, self.top, self.bottom = self.right, self.left, self.top[::-1], self.bottom[::-1]
        self.all = [line[::-1] for line in self.all]

    def check_fit(self, tile, attr, dont_change=False):
        directions = {'left': 'prev', 'right': 'next', 'top': 'above', 'bottom': 'below'}
        opposites = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bottom': 'top'}
        if dont_change:
            if getattr(self, attr) == getattr(tile, opposites[attr]):
                setattr(self, directions[attr], tile)
                return True
        
        def check_rotation():
            for i in range(3+1):
                if getattr(self, attr) == getattr(tile, opposites[attr]):
                    setattr(self, directions[attr], tile)
                    return True
                tile.rotate()
            return False
        r = check_rotation()
        if not r:
            tile.vert_flip()
            r = check_rotation()
            
        if not r:
            tile.vert_flip()
            tile.hor_flip()
            return check_rotation()
        
        return r

    def remove_borders(self):
        self.all.pop(0)
        self.all.pop(len(self.all)-1)
        self.all = [line[1:len(line)-1] for line in self.all]




tiles = []
with open("tiles.txt") as file:
    tiles = [Tile(re.search("\d+", tile).group(), tile.split(":\n")[1].split("\n")) for tile in file.read().split("\n\n")]


dragon = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")
dragon_distances = []
first = (0, 18)
for i in range(1, len(dragon)):
    for j in range(len(dragon[i])):
        if dragon[i][j] == '#':
            dragon_distances.append((i-first[0], j-first[1]))


    

def get_corners():
    corners = []
    tile_list = [tiles[0]]
    for curr in tile_list:
        neighbours = 0
        for tile in [t for t in tiles if t != curr]:
            for border in ['top', 'left', 'right', 'bottom']:
                if curr.check_fit(tile, border):
                    neighbours += 1
                    if tile not in tile_list:
                        tile_list.append(tile)
                    break
        if neighbours == 2:
            corners.append(int(curr.number))

    return corners[0]*corners[1]*corners[2]*corners[3]



def build_picture():
    puzzle = []
    line_beg = list(filter(lambda t: t.above == None and t.prev == None, tiles))[0]
    while line_beg != None:
        line = []
        curr = line_beg
        while curr != None:
            curr.remove_borders()
            line.append(curr.all)
            curr = curr.next
        line_beg = line_beg.below
        puzzle.append(line)
    return sum([[''.join(t_line) for t_line in list(zip(*line))] for line in puzzle], [])


def rotate_list(lines):
    new_lines = ['']*len(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            new_lines[j] = lines[i][j] + new_lines[j]
    return new_lines


def search_for_dragon(pic):
    count = 0
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            if pic[i][j] == '#':
                found = True
                for d in dragon_distances:
                    if not (0 <= i+d[0] < len(pic) and 0 <= j+d[1] < len(pic[i]) and pic[i+d[0]][j+d[1]] == '#'):
                        found = False
                        break
                if found:
                    count += 1
    return count


def count_dragons():
    pic = build_picture()
    def check_rotation():
        nonlocal pic
        for i in range(3+1):
            dragons = search_for_dragon(pic)
            if dragons > 0:
                return dragons
            pic = rotate_list(pic)
        return 0
            
    r = check_rotation()

    if r == 0:
        pic = pic[::-1]
        r = check_rotation()

    if r == 0:
        pic = pic[::-1]
        pic = [line[::-1] for line in pic]
        r = check_rotation()

    return '\n'.join(pic).count('#') - r*DRAGON_SIZE
 

print(get_corners())
print(count_dragons())

