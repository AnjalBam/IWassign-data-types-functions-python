"""
18. Write a Python program to check whether a given string is number or not
using Lambda.
"""

given_str1 = '45'
given_str2 = 'anjalbam'

is_number = lambda str: str.isnumeric()

print(is_number(given_str1))
print()
print(is_number(given_str2))