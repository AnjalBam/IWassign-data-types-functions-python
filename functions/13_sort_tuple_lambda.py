"""
13. Write a Python program to sort a list of tuples using Lambda.
"""

name_age = [('anjal', 20), ('alex', 9), ('Rabindra', 16), ('rajesh', 32)]

name_age.sort(key=lambda x: x[1])

print(name_age)
