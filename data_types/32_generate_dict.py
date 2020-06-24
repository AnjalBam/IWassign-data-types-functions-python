"""
32. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
dict_size = 5


def generate_dict(size):
    result_dict = {}
    for i in range(1, size + 1):
        result_dict[i] = i * i
    return result_dict


print(generate_dict(dict_size))
