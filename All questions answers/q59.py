"""
Q59. Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""


def reverse_list(lst):
    n = len(lst)
    new_list = []
    for i in range(n - 1, -1, -1):
        new_list.append(lst[i])
    return new_list


nums = [1, 2, 34, 5, 6, 7, 8, 100]

ans = reverse_list(nums)
print(ans)
