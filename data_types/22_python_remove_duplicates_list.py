"""
22. Write a program to remove duplicates from a list.
"""

sample_list = [1, 2, 5, 6, 8, 10, 5, 10, 6]

sample_list_set = set(sample_list)
list_without_duplicates = list(sample_list_set)

print(list_without_duplicates)
