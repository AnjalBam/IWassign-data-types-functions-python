"""
21. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_tuple_list(lst):
    len_lst = len(lst)
    for index in range(len_lst):
        for num in range(len_lst):
            if lst[index][1] < lst[num][1]:
                temp = lst[num]
                lst[num] = lst[index]
                lst[index] = temp

    return lst


print(sort_tuple_list(sample_list))
