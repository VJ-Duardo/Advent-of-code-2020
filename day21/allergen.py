import re

foods = []
with open("foods.txt") as file:
    foods = [(re.search(".*(?= \(contains)", food).group().split(" "),
              re.search("(?<=contains ).*(?=\))", food).group().split(", ")) for food in file.read().splitlines()]



def assign_allergens():
    allergens_dic = {}
    done = []
    for ingridients, allergens in foods:
        for a in allergens:
            if a not in allergens_dic:
                allergens_dic[a] = [i for i in ingridients if i not in done]
            else:
                allergens_dic[a] = [i for i in ingridients if i in allergens_dic[a]]
            if len(allergens_dic[a]) == 1:
                ingr = allergens_dic[a][0]
                for ingr_list in list(allergens_dic.values()):
                    if ingr in ingr_list and ingr_list is not allergens_dic[a]:
                        ingr_list.remove(ingr)
                done.append(ingr)
    return allergens_dic


def count_safe_ingredients():
    allergens_dic = assign_allergens()
    not_safe = sum(list(allergens_dic.values()), [])
    return (len(list(filter(lambda ingr: ingr not in not_safe, sum([food[0] for food in foods], [])))))


def get_unsafe_ingredients_list():
    allergens_dic = assign_allergens()
    unsafe_list = []
    for allergen in sorted(allergens_dic):
        unsafe_list.append(allergens_dic[allergen][0])
    return ','.join(unsafe_list)


print(count_safe_ingredients())
print(get_unsafe_ingredients_list())
