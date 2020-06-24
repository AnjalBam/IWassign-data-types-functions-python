"""
16. Write a Python program to sum all the items in a list.
"""

sample_list = [10, 9, 17, 25, 16]


def sum_of_items_in_list(lst):
    total_sum = 0
    for num in lst:
        total_sum += num
    return total_sum


print(sum_of_items_in_list(sample_list))
