"""
9. Write a Python program to change a given string to a new string where the
first and last chars have been exchanged.
"""
sample_str = 'Anjal Bam'


def exchange_first_last_chars(word):
    return word[-1] + word[1:-1] + word[0]


print(exchange_first_last_chars(sample_str))