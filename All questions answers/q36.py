"""
Write a function that print all the factors of a number entered by user.
"""


def print_factors():
    num = int(input("Enter a number = "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")


print_factors()
