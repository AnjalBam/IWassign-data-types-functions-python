"""
30. Write a Python script to check whether a given key already exists in a
dictionary.
"""
sample_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def check_key(dict_input, key):
    key_list = dict_input.keys()
    if list(key_list).__contains__(key):
        return True
    else:
        return False


print(check_key(sample_dict, 1))
