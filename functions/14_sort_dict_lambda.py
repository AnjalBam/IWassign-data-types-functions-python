"""
14. Write a Python program to sort a list of dictionaries using Lambda.
"""

name_marks = [
    {'name': 'Anjal', 'age': 20},
    {'name': 'Rajesh', 'age': 16},
    {'name': 'Aman', 'age': 15}
]

name_marks.sort(key=lambda x:x['age'])
print(name_marks)


