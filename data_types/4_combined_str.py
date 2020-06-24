"""
4. Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
sample_str1 = 'abc'
sample_str2 = 'xyz'


def combined_str(word1, word2):
    return f"{word2[:2] + word1[2:]} {word1[:2] + word2[2:]}"


print(combined_str(sample_str1, sample_str2))
