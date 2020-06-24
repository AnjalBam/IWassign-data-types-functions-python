"""
27. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
sample_list = [1, 3, 5, 7, 9, 10]
replace_with = [2, 4, 6, 8]


def replace_data(lst, replace_list):
    return lst[:-1] + replace_list


print(replace_data(sample_list, replace_with))
