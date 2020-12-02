sum_target = 2020
numbers = []

with open("numbers.txt", "r") as file:
    numbers = list(map(int, file.read().splitlines()))


def product(nums):
    prod = 1
    for n in nums:
        prod = prod * n
    return prod


def findRightSummands(summands, curr):
    if summands == 0:
        if sum(curr) == sum_target:
            print(curr)
            print(product(curr))
            return True
        return False
    for number in numbers:
        curr.append(number)
        if findRightSummands(summands-1, curr):
            return True
        curr.pop()


findRightSummands(2, [])
findRightSummands(3, [])
