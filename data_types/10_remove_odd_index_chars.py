"""
10. Write a Python program to remove the characters which have odd index
values of a given string.
"""
sample_str = 'I love coding.'


def remove_odd_index_chars(string):
    return string[::2]


print(remove_odd_index_chars(sample_str))

