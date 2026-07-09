"""
Q69. Given a 3x3 matrix as input, print its lower triangle.
Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

1  *  *
4  5  *
7  8  9
"""

matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 1],
    [7, 8, 9, 7],
    [9, 7, 3, 1],
]


r = len(matrix)
c = len(matrix[0])

for i in range(0, r):
    for j in range(0, c):
        if i >= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
