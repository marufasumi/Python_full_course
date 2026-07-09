"""
Q85. Dictionary Merge Function

Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries
(d1 and d2) as arguments and returns a new dictionary formed by merging them
using the update() method. Ensure d1 remains unchanged.
"""


def merge_dicts(dict1, dict2):
    new_dict = {}
    new_dict.update(dict1)
    new_dict.update(dict2)
    return new_dict


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}

ans = merge_dicts(d1, d2)
print(ans)
