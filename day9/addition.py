PREAMBLE = 25

numbers = []
with open("numbers.txt") as file:
    numbers = list(map(int, file.read().splitlines()))



def find_right_summands(array, sum_target):
    for left in array:
        for right in array:
            if left + right == sum_target and left != right:
                return True
    return False
            

def find_unlawful_number():
    for i in range (PREAMBLE, len(numbers)):
        if not find_right_summands(numbers[i-PREAMBLE:i], numbers[i]):
            return numbers[i]


def get_weakness():
    target = find_unlawful_number()
    for i in range(0, len(numbers)):
        c = []
        for j in range(i, len(numbers)):
            c.append(numbers[j])
            if sum(c) > target:
                break
            if sum(c) == target:
                return min(c) + max(c)


print(find_unlawful_number())
print(get_weakness())
