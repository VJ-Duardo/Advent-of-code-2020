import re

LENGTH = 36

values = {}
segments = []
with open("program.txt") as file:
    parts = re.split("\n(?=mask)", file.read())
    for part in parts:
        lines = part.split("\n")
        segment = [lines[0].split(" = ")[1]]
        for line in lines[1:]:
            write = line.split(" = ")
            segment.append({"mem": int(re.search("\d+", write[0]).group()),
                            "value": int(write[1])})
        segments.append(segment)



def decode_version_one(mask, value, mem):
    new_value = ""
    value_bits = format(value,'0'+str(LENGTH)+'b')
    for i in range(len(mask)):
        if mask[i] == 'X':
            new_value += value_bits[i]
        else:
            new_value += mask[i]

    values[mem] = int(new_value, 2)


def decode_version_two(mask, value, mem):
    new_address = ""
    mem_bits = format(mem,'0'+str(LENGTH)+'b')
    for i in range(len(mask)):
        if mask[i] == '1':
            new_address += '1'
        elif mask[i] == 'X':
            new_address += "{}"
        else:
            new_address += mem_bits[i]

    def fill_floating_bits(count, bits):
        if count == 0:
            values[int(new_address.format(*bits), 2)] = value
            return
        fill_floating_bits(count-1, bits+['0'])
        fill_floating_bits(count-1, bits+['1'])

    fill_floating_bits(mask.count('X'), [])


def use_masks():
    for seg in segments:
        for line in seg[1:]:
            #decode_version_one(seg[0], line["value"], line["mem"])
            decode_version_two(seg[0], line["value"], line["mem"])
    return sum(values.values())

print(use_masks())
                    
