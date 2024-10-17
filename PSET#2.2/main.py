# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #2: Remove Duplicates from a List

# This program removes duplicate elements, including nested lists, from a given list, ensuring only unique items remain

def remove_dups(list):
    new_list = []
    for item in list:
        #check if the item is not in the list
        if item not in new_list:
            new_list.append(item)
    return new_list

#valid test cases
print(remove_dups([3, 4, 3]))
print(remove_dups([3, 4, [3], [3]]))
print(remove_dups([3, 4, [3], [-2]]))
print(remove_dups([3, 4, [4, -2], [4, -2]]))
print(remove_dups([]))
print(remove_dups([[]]))
print(remove_dups([[], []]))
print(remove_dups([5, 5, 1]))
print(remove_dups([7, 6, [2, -7], [2, -7]]))

#invalid test cases
print(remove_dups([1, [2, [3]], [2, [3]]]))
print(remove_dups([4, {2, 5}, {2, 5}, [3]]))