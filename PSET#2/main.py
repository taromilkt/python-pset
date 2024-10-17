# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #1: Reverse an Integer

# This program shows the reversed digits of a 32-bit integer, keeping the sign. If the result is too large or small, it shows 0.

def reverse_integer(x:int) -> int:
    #define range limits for singed 32 bit integers
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    result = 0
    negative = x < 0
    x = abs(x)

    #convert x to a list of digits by getting the length of the number
    digits = []
    while x != 0:
        digits.append(x % 10)
        x //= 10

    #use for loop to repeat over digits and build reversed number
    for num in digits:
        if result > (INT_MAX - num) //10:
            return 0
        result = result * 10 + num

    if negative:
        result = -result

    if result < INT_MIN or result > INT_MAX:
        return 0

    return result

if __name__ == '__main__':
    # valid test cases
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(204))

    #invalid test cases
    print(reverse_integer(50.5))
    print(reverse_integer(-1763847412))