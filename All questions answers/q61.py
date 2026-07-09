"""
Q61. Given a list, remove all duplicate elements while preserving the original
order of the unique items.
"""


def remove_duplicates(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result


nums = [1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]
print(remove_duplicates(nums))
