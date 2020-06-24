"""
5. Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""


def fact(num):
    if num > 0:
        product = 1
        for i in range(1, num + 1):
            product *= i
        return product
    else:
        return None


print(fact(5))
