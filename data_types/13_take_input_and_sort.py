"""
13. Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
sample_input = input('Enter strings separated by commas: ')

word_list = sample_input.split(', ')

print(sorted(word_list))





