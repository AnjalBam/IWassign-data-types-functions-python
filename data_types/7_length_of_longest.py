"""
7. Write a Python function that takes a list of words and returns the length of
 the longest one.
"""

sample_list = ['Anjal', 'Rabindra', 'code', 'Engineering']


def length_of_longest(lst):
    len_of_longest_word = 0
    for word in lst:
        if len(word) > len_of_longest_word:
            len_of_longest_word = len(word)

    return len_of_longest_word


print(length_of_longest(sample_list))