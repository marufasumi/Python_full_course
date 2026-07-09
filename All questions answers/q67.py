"""
Q67. Given a list of marks, use list comprehension to create a new list that contains
only the marks that are above 75.
"""

marks = [45, 87, 15, 94, 37, 89, 90, 99, 32, 11]
new_list = [num for num in marks if num >= 75]
print(marks, id(marks))
print(new_list, id(new_list))
