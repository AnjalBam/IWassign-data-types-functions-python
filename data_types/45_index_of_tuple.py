"""
45. Write a Python program to find the index of an item of a tuple.
"""
sample_tuple_input = ('I', 'love', 'python')


def find_index(sample_tuple, value):
    return sample_tuple.index(value)


print(find_index(sample_tuple_input, 'love'))

