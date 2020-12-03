tree_lines = []
tree_counts = []
tree = '#'

with open("area.txt", "r") as file:
    tree_lines = list(file.read().splitlines())


def product(nums):
    prod = 1
    for n in nums:
        prod = prod * n
    return prod


def count_trees(right, down):
    curr = 0
    tree_count = 0
    
    for i in range(down, len(tree_lines), down):
        curr = curr+right
        while curr > len(tree_lines[i])-1:
            tree_lines[i] += tree_lines[i]

        if tree_lines[i][curr] == tree:
            tree_count += 1

    print(tree_count)
    return tree_count

tree_counts.append(count_trees(1, 1))
tree_counts.append(count_trees(3, 1))
tree_counts.append(count_trees(5, 1))
tree_counts.append(count_trees(7, 1))
tree_counts.append(count_trees(1, 2))
print(product(tree_counts))


        
