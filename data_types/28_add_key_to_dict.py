"""
28. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
sample_dict = {0: 10, 1: 20}


def add_key(prev_dict, key, value):
    prev_dict[key] = value
    return prev_dict


print(add_key(sample_dict, 2, 30))
