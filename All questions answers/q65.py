"""
Q65. Write a Python script that iterates through a list of integers and replaces every
negative number found in the list with the value 0.
"""


def replace_negative(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


nums = [1, 4, -1, -45, -100, 6, 7, 8, -1]
print(replace_negative(nums))
