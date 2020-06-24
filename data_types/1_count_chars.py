"""
1. Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
sample_str = "google.com"

word_count = {}

for char in sample_str:
    count = 0
    for c in sample_str:
        if char == c:
            count += 1
    word_count[char] = count

print(word_count)
