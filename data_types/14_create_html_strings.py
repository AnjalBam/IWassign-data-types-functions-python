"""
14. Write a Python function to create the HTML string with tags around the
word(s).
"""

sample_str = 'I love programming Python.'
sample_tag = 'i'


def add_tags(tag, content):
    return f"<{tag}>{content}</{tag}>"


print(add_tags(sample_tag, sample_str))
