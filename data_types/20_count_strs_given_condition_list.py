"""
20. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
sample_list = ['abc', 'xyz', 'aba', '1221', 'eagle']


def count_strings(lst):
    count = 0
    for item in lst:
        if item[0] == item[-1] and len(item) >= 2:
            count += 1

    return count


print(count_strings(sample_list))
