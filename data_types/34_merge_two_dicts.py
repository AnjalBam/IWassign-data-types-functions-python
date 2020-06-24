"""
34. Write a Python script to merge two Python dictionaries.
"""
dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
dict2 = {7: 49, 8: 64, 9: 81, 10: 100, 11: 121}
merged_dicts = {}

merged_dicts.update(dict1)
merged_dicts.update(dict2)

print(merged_dicts)
