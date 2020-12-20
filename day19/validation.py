rules = {}
messages = []
with open("messages.txt", "r") as file:
    sections = file.read().replace('"', '').split("\n\n")
    for line in sections[0].split("\n"):
        entry = line.split(": ")
        rules[entry[0]] = entry[1] if entry[1] in ['a', 'b'] else [part.split(" ") for part in entry[1].split(" | ")]
    messages = sections[1].split("\n")



def validate(message):
    def check(rule, msg):
        if rules[rule] in ['a', 'b']:
            if(len(msg) == 0):
                return (True, msg)
            if rules[rule] == msg[0]:
                return (True, msg[1:])
            else:
                return (False, msg)
        backup = ''.join(list(msg).copy())
        for i in range(len(rules[rule])):
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
    if len(result[1]) == 0:
        print(message)
        return True
    else:
        return False


def count_valid_messages():
    c = 0
    for msg in messages:
        if validate(msg):
            c += 1
    return c

#print(count_valid_messages())

rules['8'] = [['42'], ['42', '8']]
rules['11'] = [['42', '31'], ['42', '11', '31']]
print(count_valid_messages())

