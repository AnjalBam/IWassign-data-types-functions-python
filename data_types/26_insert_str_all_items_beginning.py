"""
26. Write a Python program to insert a given string at the beginning of all
items in a list.
Sample list : [1,2,3,4], string : emp
"""
sample_list = ['a', 'b', 'c', 'd', 'e']
# sample_list = [1, 2, 3, 4, 5, 6]


def insert_str_beginning_each(lst, string):
    for index in range(len(lst)):
        lst[index] = string + str(lst[index])

    return lst


print(insert_str_beginning_each(sample_list, 'code '))
