"""
7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
sample_str = 'The quick Brown Fox'


def count_upper_lower(string):
    temp_list = list(string)
    upper_count = 0
    lower_count = 0
    for s in temp_list:
        if s.isupper():
            upper_count += 1
        else:
            lower_count += 1

    return upper_count, lower_count


upper, lower = count_upper_lower(sample_str)
print(f"upper: {upper}, lower: {lower}")
