"""
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""
sample_list = [8, 2, 3, -1, 7]


def multiply_all_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product


print(multiply_all_elements(sample_list))
