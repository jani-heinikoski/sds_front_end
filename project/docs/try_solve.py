# Author: Jani Heinikoski
# Last modified: 05.03.2021
# Sources: -
# Description: Tries to solve the sudoku below (None represents empty cell)
sudoku = [
    [7, 2, 6, 3, 1, None, 4, 8, 5],
    [5, None, None, None, 8, 2, None, None, 6],
    [9, 4, 8, 6, 5, 7, 1, 3, None],
    [None, 9, None, 2, None, None, None, None, 7],
    [2, 7, 3, 8, 4, 5, 6, 1, None],
    [None, None, None, None, None, 1, None, 2, None],
    [3, 8, 2, 7, 9, 4, 5, 6, None],
    [6, None, None, 5, 2, None, None, None, 8],
    [4, 5, None, None, None, None, None, 9, 3]
]
# Formatted printing for the sudoku
def print_sudoku():
    print("##############################################")
    for i in range (0, 9):
        for j in range (0, 9):
            print("%d, " % (sudoku[i][j]), end="")
        print()
    print("##############################################")
# Returns the first None cell it finds
def next_available():
    for i in range (0, 9):
        for j in range (0, 9):
            if (sudoku[i][j] == None):
                return (i, j)
    return None, None
# Checks if num is in 3x3 grid defined by i, j which are
# the top-left coordinates of the 3x3 grid in sudoku matrix
def in_3by3(num, i, j):
    three_by_three = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    for x in range (0, 3):
        for y in range (0, 3):
            three_by_three[x][y] = sudoku[i+x][j+y]
    if (num in three_by_three):
        return False
    else:
        return True
# Checks if num fits the cell at sudoku[i][j]
def fits(num, i, j):
    # Check rows and cols
    for x in range (0, 9):
        if (sudoku[i][x] == num or sudoku[x][j] == num):
            return False
    # Check the 3x3 grids
    if (i >= 0 and i <= 2):
        if (j >= 0 and j <= 2):
            return in_3by3(num, 0, 0) # left-top
        elif (j >= 3 and j <= 5):
            return in_3by3(num, 0, 3) # center-top
        elif (j >= 6 and j <= 8):
            return in_3by3(num, 0, 6) # right-top
    elif (i >= 3 and i <= 5):
        if (j >= 0 and j <= 2):
            return in_3by3(num, 3, 0) # left-mid
        elif (j >= 3 and j <= 5):
            return in_3by3(num, 3, 3) # center-mid
        elif (j >= 6 and j <= 8):
            return in_3by3(num, 3, 6) # right-mid
    elif (i >= 6 and i <= 8):
        if (j >= 0 and j <= 2):
            return in_3by3(num, 6, 0) # left-bottom
        elif (j >= 3 and j <= 5):
            return in_3by3(num, 6, 3) # center-bottom
        elif (j >= 6 and j <= 8):
            return in_3by3(num, 6, 6) # right-bottom
    else:
        print("ERROR: i=%d j=%d out of range" % (i, j))
        exit(-1)
# Replaces -1's with Nones
def reset_nones():
    replaced = False
    for x in range(0, 9):
        for y in range(0, 9):
            if (sudoku[x][y] == -1):
                replaced = True
                sudoku[x][y] = None
    return replaced
# Main functionality, solves the sudoku using above funcs
def solve():
    number_found = False
    for x in range(0, 9):
        for y in range(0, 9):
            i, j = next_available()
            true_count = 0
            n = -1
            # If no more empty cells, print the sudoku
            if (i == None or j == None):
                print_sudoku()
                # Try again if a cell was filled in last try
                if (number_found == True):
                    if (reset_nones()):
                        solve()
                return
            # Try all numbers in the cell sudoku[i][j]
            for z in range(1, 10):
                if (fits(z, i, j)):
                    true_count += 1
                    n = z
            # If only one number fits in cell sudoku[i][j]
            # insert it, else insert -1
            if (true_count == 1):
                number_found = True
                sudoku[i][j] = n
            else:
                sudoku[i][j] = -1

if __name__ == "__main__":
    solve()