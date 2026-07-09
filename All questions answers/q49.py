"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie
from your list using both positive and negative indexing where appropriate.
"""

marks = [54, 21, 56, 76, 787, 453, 432, 43, 100, 11, 32, 1, 54, 65765, 98, 100]

n = len(marks)
print(f"First element = {marks[0]}")
print(f"Last element = {marks[-1]}")
print(f"Middle element = {marks[n//2]}")
