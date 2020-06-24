"""
15. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
sample_str = 'PHP'
surrounding_text = '{{}}'


def insert_string_middle(surround_text, text):
    mid_of_surrounding_text = len(surround_text) // 2
    return (surround_text[:mid_of_surrounding_text]
            + text + surround_text[mid_of_surrounding_text:])


print(insert_string_middle(surrounding_text, sample_str))
