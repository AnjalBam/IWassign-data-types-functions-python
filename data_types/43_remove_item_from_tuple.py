"""
43. Write a Python program to remove an item from a tuple.
"""
sample_tuple = ('I', 'love', 'python')

temp_list = list(sample_tuple)

temp_list.pop()
result_tuple = tuple(temp_list)
print(result_tuple)

