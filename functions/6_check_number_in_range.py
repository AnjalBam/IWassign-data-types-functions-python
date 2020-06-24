"""
6. Write a Python function to check whether a number is in a given range.
"""


def check_num(lower_range, upper_range, num):
    for i in range(lower_range, upper_range):
        if i == num:
            return True
    return False


print(check_num(2, 10, 7))
