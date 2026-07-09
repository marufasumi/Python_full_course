"""
Ask a number from the user, and count all the factors.

Enter a number = 10
4

Enter a number = 100
9
"""

num = int(input("Enter num = "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i += 1

print(f"Total factors of {num} are {count}")
