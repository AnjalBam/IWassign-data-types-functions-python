"""
6. Write a Python program to find the first appearance of the substring 'not'
 and 'poor' from a given string, if 'not' follows the 'poor', replace the
 whole 'not'...'poor'
substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
sample_str = 'The lyrics is not not poor!'


def check_if_poor(input_word):
    index_of_not = input_word.find('not')
    index_of_poor = input_word.find('poor')
    if index_of_not > 0 < index_of_poor > 0:
        return input_word.replace(input_word[
                                  index_of_not: index_of_poor + 4], 'good')
    else:
        return input_word


print(check_if_poor(sample_str))
