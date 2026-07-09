"""
Q102. Longest Word

Take a sentence as input. Print the longest word in it.
"""


def print_longest_word(sentence: str):
    words = sentence.split()
    print(max(words, key=lambda x: len(x)))
    # longest_count = 0
    # longest_word = ""
    # for word in words:
    #     if len(word) > longest_count:
    #         longest_count = len(word)
    #         longest_word = word
    # print(longest_word)


sentence = "Anirudh is learning Python programming every single day"
print_longest_word(sentence)
