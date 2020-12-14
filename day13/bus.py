TIMESTAMP = 0
bus_plan = []

with open("notes.txt") as file:
    lines = file.read().splitlines()
    TIMESTAMP = int(lines[0])
    bus_plan = lines[1].split(',')


def get_earliest_bus(busses):
    busses = [int(bus) for bus in busses if bus != 'x']
    busses.sort(key = lambda b: b - (TIMESTAMP % b))
    return busses[0]*(busses[0] - (TIMESTAMP % busses[0]))


def prod(nums):
    prod = 1
    for n in nums:
        prod = prod * n
    return prod

def extend_eucl(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = extend_eucl(b % a, a)
        return (y - (b//a) * x, x)

def get_earliest_timestamp(busses):
    a_list = [0]
    m_list = [int(busses[0])]
    for i in range(1, len(busses)):
        if busses[i] != 'x':
            a_list.append(int(busses[i])-i)
            m_list.append(int(busses[i]))
            
    n = prod(m_list)
    n_list = [n//mn for mn in m_list]
    
    result = sum([prod([a_list[i], extend_eucl(m_list[i], n_list[i])[1], n_list[i]]) for i in range(len(a_list))])
    if result > TIMESTAMP:
        while result > TIMESTAMP: result -= n
        return result+n
    else:
        while result < TIMESTAMP: result += n
        return result
    

print(get_earliest_bus(bus_plan.copy()))
print(get_earliest_timestamp(bus_plan))
