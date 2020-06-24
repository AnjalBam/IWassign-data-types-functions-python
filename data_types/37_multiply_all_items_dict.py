"""
37. Write a Python program to multiply all the items in a dictionary.
"""
sample_dict = {'a': 2, 'b': 4, 'c': 8, 'd': 10, 'e': 2}
final_product = 1
for value in sample_dict.values():
    final_product *= value

print(final_product)

