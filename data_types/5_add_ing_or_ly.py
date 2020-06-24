"""
5. Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
sample_str = 'string'  # input can be varied


def add_ing_or_ly(word):
    if len(word) < 3:
        return word
    else:
        if word[-3:] == 'ing':
            return word + 'ly'
        else:
            return word + 'ing'


print(add_ing_or_ly(sample_str))
