import re

class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = {}

    def add_bag(self, amount, bag):
        self.contains[bag] = amount


bags = {}
with open("rules.txt", "r") as file:
    rules = file.read().splitlines()
    for rule in rules:
        bags_list = re.findall("^\w+ \w+(?= bag)|\d \w+ \w+(?= bag)", rule)
        parent = bags_list[0]
        if parent not in bags.keys():
            bags[parent] = Bag(parent)

        for child in bags_list[1:]:
            child_name = child[2:]
            if child_name not in bags.keys():
                bags[child_name] = Bag(child_name)
            bags[parent].add_bag(child[:1], bags[child_name])


def count_bag_contains(bag_name):
    def search_bag(curr_bag):
        if curr_bag.name == bag_name:
            return True

        for child_bag in curr_bag.contains.keys():
            if search_bag(child_bag):
                return True

    count = 0
    for bag in bags.keys():
        if search_bag(bags[bag]):
            count += 1
    return count-1


def count_required_bags(amount, bag):
    c = 0
    for child_bag in bag.contains.keys():
        if len(child_bag.contains) < 1:
            c += int(bag.contains[child_bag])
        else:
            c += int(count_required_bags(bag.contains[child_bag], child_bag))
    return int(amount) + c * int(amount)


print(count_bag_contains("shiny gold"))
print(count_required_bags(1, bags["shiny gold"])-1)
        
