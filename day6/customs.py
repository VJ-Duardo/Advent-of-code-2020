answers = [] 
with open("answers.txt", "r") as file:
    answers = file.read().split("\n\n")


def sum_counts():
    return sum([len(set("".join(answer.split("\n")))) for answer in answers])


def sum_counts_correctly():
    return sum([len(set.intersection(*[set(line) for line in answer.split("\n")])) for answer in answers])


print(sum_counts())
print(sum_counts_correctly())
