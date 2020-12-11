adapters = []
with open("adapters.txt") as file:
    adapters = list(map(int, file.read().splitlines()))
    adapters.append(0)
    adapters.sort()
    

def get_multiplied_differences():
    differences = {1: 0, 3: 1}
    for i in range(1, len(adapters)):
        differences[adapters[i]-adapters[i-1]] += 1
    return differences[1]*differences[3]


def count_arrangements():
    f = [1]
    for i in range(1, len(adapters)):
        a = 0
        for j in range(1, 3+1):
            if adapters[i]-adapters[i-j] <= 3 and i-j >= 0:
                a += f[i-j] 
        f.append(a)
    return f[len(f)-1]
    
print(get_multiplied_differences())
print(count_arrangements())
