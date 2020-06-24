"""
11. Write a Python program to count the occurrences of each word in a given
sentence.
"""
sample_sentence = 'Python programming is easy and it is fun programming it too.'


def count_words(sentence):
    word_list = sentence.split(' ')
    word_count = {}
    for word in word_list:
        count = 0
        for test_word in word_list:
            if test_word == word:
                count += 1
        word_count[word] = count

    return word_count


print(count_words(sample_sentence))
