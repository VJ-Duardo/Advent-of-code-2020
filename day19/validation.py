rules = {}
messages = []
with open("messages.txt", "r") as file:
    sections = file.read().replace('"', '').split("\n\n")
    for line in sections[0].split("\n"):
        entry = line.split(": ")
        rules[entry[0]] = entry[1] if entry[1] in ['a', 'b'] else [part.split(" ") for part in entry[1].split(" | ")]
    messages = sections[1].split("\n")


def validate(message, normal=True):
    invalid = False
    b = True
    def check(rule, msg):
        nonlocal invalid, b
        if rules[rule] in ['a', 'b']:
            if(len(msg) == 0):
                invalid = True
                return (b, msg)
            if rules[rule] == msg[0]:
                return (True, msg[1:])
            else:
                return (False, msg)
        for i in range(len(rules[rule])):
            backup = ''.join(list(msg).copy())
            fits = True
            for j in range(len(rules[rule][i])):
                result, msg = check(rules[rule][i][j], msg)
                if not result:
                    fits = False
                    break
            if fits:
                return (True, msg)
            else:
                msg = backup
        return (False, msg)
    result = check("0", message)
    if normal:
        return len(result[1]) == 0
    switch_list()
    b = False
    invalid = False
    check("0", message)
    switch_list()
    return (len(result[1]) == 0 and not invalid)
        

def switch_list():
    rules['8'][0], rules['8'][1] = rules['8'][1], rules['8'][0]
    rules['11'][0], rules['11'][1] = rules['11'][1], rules['11'][0]

def count_valid_messages(normal=True):
    c = 0
    for msg in messages:
        if validate(msg, normal):
            c += 1
    return c

print(count_valid_messages())

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
print(count_valid_messages(False))

