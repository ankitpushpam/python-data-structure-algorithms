"""
PROBLEM 1:

Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

For example, if n=4 , return 4+3+2+1+0, which is 10.
"""

def rec_sum(n):
    if n == 0:
        return 0

    else:
        return n + rec_sum(n-1)

print(rec_sum(4))

"""
Problem 2
Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1

"""

def digit_sum(n):
    if len(str(n)) == 1:
        return n

    else:
        return n%10 + digit_sum(n//10)

print(digit_sum(4321))