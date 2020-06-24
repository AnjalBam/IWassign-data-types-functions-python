"""
19. Write a Python program to get the smallest number from a list.
"""
sample_list = [10, 34, 67, 25, 85, 12, 2]


def find_smallest_num(lst):
    sorted_list = sorted(lst)
    return sorted_list[0]


print(find_smallest_num(sample_list))
