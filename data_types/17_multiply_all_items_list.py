"""
17. Write a Python program to multiply all the items in a list.
"""
sample_list = [7, 4, 8, 2, 9]


def multiply_items_in_list(lst):
    product = 1
    for item in lst:
        product *= item
    return product


print(multiply_items_in_list(sample_list))
