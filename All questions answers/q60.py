"""
Q60. Given two lists, merge them into a single new list without modifying the originals.
"""

# def merge_two_lists(lst1, lst2):
#     return lst1 + lst2


def merge_two_lists(lst1, lst2):
    new_list = []
    for num in lst1:
        new_list.append(num)
    for num in lst2:
        new_list.append(num)
    return new_list


num1 = [1, 2, 3]
num2 = [65, 32, 11]
print(merge_two_lists(num1, num2))
