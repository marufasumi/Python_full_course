"""
Q73. Given a 4x4 matrix, print only the border elements and replace the
inner elements with an asterisk (*).
"""

# define the 4x4 matrix

# border condition: element is on the first row, last row, first column, or last column
# inner elements: row index is not 0 or 3, AND column index is not 0 or 3

# loop through each row using its index

    # loop through each column index in that row

        # if the element is on the border (first/last row or first/last col) -> print the element

        # otherwise it's an inner element -> print "*"

    # print a newline after each row
