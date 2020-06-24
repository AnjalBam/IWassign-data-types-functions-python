"""
11. Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""

# function to add 15
add_15 = lambda num: num + 15

print(add_15(10))
print()
print()
# function to multiply two args
multiply_two = lambda num1, num2: print(num2 * num1)

multiply_two(10, 10)
