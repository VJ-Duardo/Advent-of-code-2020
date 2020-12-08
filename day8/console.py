instructions = []
with open("instructions.txt", "r") as file:
    for line in file:
        parts = line.split(" ")
        instructions.append([parts[0], int(parts[1])])


def count_acc(instr_list):
    marked = []
    i = 0
    acc = 0
    while i not in marked:
        if i > len(instr_list)-1:
            return (True, acc)
        marked.append(i)
        instr, val = instructions[i][0], instructions[i][1]
        if instr == "nop":
            i += 1
        elif instr == "acc":
            acc += int(val)
            i += 1
        elif instr == "jmp":
            i += int(val)
    return (False, acc)


def count_fixed_acc(instr_list):
    swap = {"nop": "jmp", "jmp": "nop"}
    for i in range(0, len(instr_list)):
        instr = instr_list[i][0]
        if instr == "acc":
            continue
        instr_list[i][0] = swap[instr]
        result = count_acc(instr_list)
        if result[0]:
            return result[1]
        instr_list[i][0] = swap[swap[instr]]
        

print(count_acc(instructions)[1])
print(count_fixed_acc(instructions))
