"""
8. Write a Python function that takes a list and returns a new list with unique
elements of the first list.

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
sample_list = [1,2,3,3,3,3,4,5]


def get_unique_list(lst):
    temp_set = set(lst)
    return list(temp_set)


print(get_unique_list(sample_list))
