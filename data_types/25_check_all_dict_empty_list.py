"""
25. Write a Python program to check whether all dictionaries in a list are empty or
not.

Sample list : [{},{},{}]
Return value : True

Sample list : [{1,2},{},{}]
Return value : False

"""
sample_list = [{},{},{}]
# sample_list = [{1: 2},{},{}]


def check_if_all_empty(lst):
    is_empty = True
    for dict_item in lst:
        if len(dict_item.items()) != 0:
            is_empty = False
            break

    return is_empty


print(check_if_all_empty(sample_list))
