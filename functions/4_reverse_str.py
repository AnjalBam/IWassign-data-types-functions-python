"""
4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
sample_str = "1234abcd"


def reverse_str(string):
    return string[-1::-1]


print(reverse_str(sample_str))