cups = []
with open("cups.txt") as file:
    cups = list(map(int, list(file.read())))

MAX_LABEL = 1000000


class Node:
    def __init__(self, label, after):
        self.label = label
        self.after = after

def do_moves(cups_dic, moves):
    curr = cups_dic[cups[0]]
    for j in range(moves):
        select = [curr.after, curr.after.after, curr.after.after.after]
        curr.after = select[2].after

        destination_label = curr.label-1
        while destination_label >= 1 and cups_dic[destination_label] in select:
            destination_label = destination_label-1
        if destination_label < 1:
            destination_label = MAX_LABEL
        destination = cups_dic[destination_label]

        select[2].after = destination.after
        destination.after = select[0]
            
        curr = curr.after

    return cups_dic[1].after.label * cups_dic[1].after.after.label
    #return ''.join([str(e) for e in cups[cups.index(1)+1:]+cups[:cups.index(1)]])


def get_cups_dic(length):
    for i in range(max(cups)+1, length+1):
        cups.append(i)

    prev = Node(cups[0], None)
    cups_dic = {cups[0]: prev}
    for c in cups[1:]:
        prev.after = Node(c, None)
        prev = prev.after
        cups_dic[c] = prev
    prev.after = cups_dic[cups[0]]

    return cups_dic


print(do_moves(get_cups_dic(1000000), 10000000))


    
    
