"""
12. Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""


def multiply_with(num):
    return lambda given_num: given_num * num


mul = multiply_with(10)
print(mul(9))
