"""
40. Write a Python program to add an item in a tuple.
"""
sample_tuple = (10, 20, 30)

temp_list = list(sample_tuple)
temp_list.append(40)

result_tuple = tuple(temp_list)
print(result_tuple)
