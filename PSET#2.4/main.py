# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #4: Consecutive Zeros

# This program sorts out the string to find the most 0's in a group.

def consecutive_zeros(binary_str):
    #split the string by '1' to find the length of the 0's
    zero_groups = binary_str.split('1')
    max_consecutive_zeros = max(len(string) for string in zero_groups)
    return max_consecutive_zeros

if __name__ == '__main__':
    #valid test cases
    print(consecutive_zeros("1001101000110"))
    print(consecutive_zeros("100011010001100000"))
    print(consecutive_zeros("1100011010001100011"))
    print(consecutive_zeros("1010101010100000"))
    print(consecutive_zeros("100100000100000010000101000000000100000"))
    print(consecutive_zeros("100101"))
    print(consecutive_zeros("10010001000010000001000001001010101001001"))

    #invalid test cases
    print(consecutive_zeros("110 010"))
    print(consecutive_zeros("1001a2410"))

