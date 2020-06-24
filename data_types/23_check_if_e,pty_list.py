"""
23. Write a program to check if the list is empty or not.
"""
sample_list = [1, 3, 5, 6, 7]
# sample_list = []


def check_if_empty(list):
    if len(list) == 0:
        return 'Empty List!'
    else:
        return 'List Not Empty!'


print(check_if_empty(sample_list))
