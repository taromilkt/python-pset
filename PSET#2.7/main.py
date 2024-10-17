# programmer: Lindsey Nguyen
# date of submission: 10/23/2024

# PSET 2
# ==============================

# Problem #5: Climbing Steps

# This program calculates the number of distinct ways to climb a staircase with n steps, where you can take either 1 or 2 steps at a time.

def climbStairs(n:int) -> int:
    one, two = 1,1
    for i in range (n-1):
        temp = one
        one = one + two
        two = temp
    return one

#valid test cases
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))

#invalid test cases
print(climbStairs(-1))
print(climbStairs(2.5))

