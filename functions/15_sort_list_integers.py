"""
15. Write a Python program to filter a list of integers using Lambda.
"""
sample_list = [2, 4, 5, 12, 13, 23, 98, 99]

odd_items = list(filter(lambda x: x % 2 != 0, sample_list))

print(odd_items)

