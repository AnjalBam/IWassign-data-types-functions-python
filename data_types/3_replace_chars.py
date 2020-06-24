"""
3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
sample_str = 'characters'

replaced = sample_str.replace(sample_str[0], '$')

print(sample_str[0]+replaced[1:])
