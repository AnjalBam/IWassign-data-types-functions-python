"""
16. Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""
sample_list = [2, 4, 5, 12, 13, 23, 98, 99]

squared = list(map(lambda x: x * x, sample_list))
print(squared)

cubed = list(map(lambda num: num ** 3, sample_list))
print(cubed)
