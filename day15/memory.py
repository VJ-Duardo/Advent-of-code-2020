#END = 2020
END = 30000000

turns = {}
with open("numbers.txt") as file:
    start_numbers = list(map(int, file.read().split(',')))
    for i in range(len(start_numbers)):
        turns[start_numbers[i]] = [i+1]


def get_last_spoken_number():
    latest = list(turns)[-1:][0]
    for i in range(len(turns), END):
        next_number = 0
        if len(turns[latest]) == 2:
            next_number = turns[latest][1] - turns[latest][0]
        if next_number not in turns:
            turns[next_number] = [i+1]
        else:
            if len(turns[next_number]) == 2:
                turns[next_number].pop(0)
            turns[next_number].append(i+1)
        latest = next_number
    return latest


print(get_last_spoken_number())
