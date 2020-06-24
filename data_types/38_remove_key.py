"""
38. Write a Python program to remove a key from a dictionary.
"""
sample_dict = {'a': 2, 'b': 4, 'c': 8, 'd': 10, 'e': 2}


def remove_key(dict_item, key):
    dict_item.pop(key)


remove_key(sample_dict, 'a')
print(sample_dict)
