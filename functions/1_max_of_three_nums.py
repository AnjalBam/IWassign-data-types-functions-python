"""
1. Write a Python function to find the Max of three numbers.
"""


def max_of_three_nums(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is the greatest."
    elif num2 > num1 and num2 > num3:
        return f"{num2} is the greatest."
    else:
        return f"{num3} is the greatest."


print(max_of_three_nums(10, 220, 30))