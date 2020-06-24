"""
8. Write a Python program to remove the n
th
index character from a nonempty

string.
"""

sample_str = 'Hello Nepal'
input_index = 4


def remove_from_index(word, index):
    if len(word) > 0:
        word_lst = list(word)
        word_lst.pop(index)
        return ''.join(word_lst)
    else:
        raise AttributeError('Empty string')


print(remove_from_index(sample_str, input_index))
