# Chapter 7: Auto-Graded Programming Project 2
# Unlimited tries
# A Magic Square is a grid with 3 rows and 3 columns with the following properties:
# The grid contains every number from 1 to 9.
# The sum of each row, each column, and each diagonal all add up to the same number.
# This is an example of a Magic Square:
# 4 9 2
# 3 5 7
# 8 1 6 
# In Python, you can simulate a 3x3 grid using a two-dimensional list. For example, the list corresponding to the grid above would be: [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# Write the definition of a function named is_magic_square that accepts a two-dimensional list as an argument and returns either True or False to indicate whether the list is a Magic Square. (Submit only the function definition, not a complete program.)
# Note: Here are some magic squares that you can use to test your function in development:
# [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
# [[6, 1, 8], [7, 5, 3], [2, 9, 4]]

def is_magic_square(grid):
    # Calculate the sum of the first row to be used as a reference sum
    ref_sum = sum(grid[0])

    # Check rows
    for row in grid:
        if sum(row) != ref_sum:
            return False

    # Check columns
    for col in range(len(grid)):
        column_sum = sum(grid[row][col] for row in range(len(grid)))
        if column_sum != ref_sum:
            return False

    # Check diagonals
    diagonal1_sum = sum(grid[i][i] for i in range(len(grid)))
    diagonal2_sum = sum(grid[i][len(grid) - 1 - i] for i in range(len(grid)))
    if diagonal1_sum != ref_sum or diagonal2_sum != ref_sum:
        return False

    return True