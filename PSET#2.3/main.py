# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #3: Two Sum

# This program finds two numbers in a list that add up to a given target.

def two_sum(num_list, target):
    num_dict = {}

    for i, num in enumerate(num_list):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], i]
        num_dict[num] = i
    return

if __name__ == '__main__':
    #valid test cases
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3, 3], 6))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([1, 4, 5],6))
    print(two_sum([2, 6, 7], 8))
    print(two_sum([1, 5, 6], 7))
    print(two_sum([2, 2], 4))

    #invalid test cases
    print(two_sum([2, 5], 10))
    print(two_sum([2], 4))