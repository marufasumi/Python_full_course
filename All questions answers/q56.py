"""
Given two lists of the same length, write Python code using a loop to create
a new list where each element is the sum of the corresponding elements from
both original lists.
"""


def sum_of_two_list(lst1, lst2):
    new_list = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list


nums1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
nums2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]
ans = sum_of_two_list(nums1, nums2)
print(ans)
