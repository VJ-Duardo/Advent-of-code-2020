tasks = []
with open("homework.txt") as file:
    tasks = [list(t.replace(" ", "")) for t in file.read().splitlines()]


def get_other_bracket(inpt, start):
    options = {'(': 1, ')': -1}
    brackets = 1
    i = start
    while brackets != 0:
        i += options[inpt[start]]
        if inpt[i] == '(':
            brackets += options[inpt[start]]
        elif inpt[i] == ')':
            brackets -= options[inpt[start]]
    return i


def solve_math(ex, precedence):
    i = 0
    while i < len(ex):
        if ex[i] in precedence:
            inserts = []
            for n in [i-1, i+1]:
                if ex[n] in [')', '(']:
                    inserts.append(get_other_bracket(ex, n))
                else:
                    inserts.append(n)

            ex.insert(inserts[0], '(')
            ex.insert(inserts[1]+2, ')')
            i += 1
        i += 1
        
    return eval(''.join(ex))


def solve_all(precedence):
    return sum([solve_math(task.copy(), precedence) for task in tasks])

print(solve_all(['*', '+']))
print(solve_all(['+']))
