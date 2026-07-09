"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.
"""


# 3 number, are different
def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)


find_max(1, 2, 3)
find_max(65, -10, 44)
