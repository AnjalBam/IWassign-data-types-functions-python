"""
18. Write a Python program to get the largest number from a list.
"""
sample_list = [10, 34, 67, 25, 85, 12]


def find_largest_num(lst):
    sorted_list = sorted(lst)
    return sorted_list[-1]


print(find_largest_num(sample_list))
