"""
17. Write a Python program to find if a given string starts with a given
character using Lambda.
"""
sample_str = 'coding'

check_if_starts = lambda char: True if char == sample_str[0] else False

print(check_if_starts('c'))  # True
print()
print(check_if_starts('d'))  # False
