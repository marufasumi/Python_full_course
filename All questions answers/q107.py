"""
Q107. Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in
each word). Example: "Python is fun" -> "fun is Python".
"""


def reverse_words(sentence: str):
    words = sentence.split()
    words = words[::-1]
    return " ".join(words)


sentence = "Anirudh is learning Python programming every single day"
print(reverse_words(sentence))
