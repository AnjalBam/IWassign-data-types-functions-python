"""
10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_even_numbers(lst):
    even_list = []
    for item in lst:
        if item % 2 == 0:
            even_list.append(item)
    print(even_list)


print_even_numbers(sample_list)