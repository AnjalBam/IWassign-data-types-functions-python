"""
20. Write a Python program to find intersection of two given arrays using
Lambda.
"""
array1 = [2, 3, 6, 9, 10]
array2 = [10, 18, 25, 2, 6]

intersection_of_arrays = filter(lambda x: x in array1, array2)
print(list(intersection_of_arrays))
