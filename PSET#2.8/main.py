# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #5: Find interesting words

# This program converts a nested list (lists within lists) into a flat list containing all the elements in their original order.

def flatten(aList):
    flattened_list = []

    for item in aList:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)

    return flattened_list

#valid test cases
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, [2,6,7]], [3, 4]]))
print(flatten([0, [[1,9], 5, [2,6,7], [3, 4]]]))

#invalid test cases
print(flatten(478))
print(flatten(([1, 2, None, [3, 4]])))
