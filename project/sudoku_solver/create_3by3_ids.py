# Author: Jani Heinikoski
# Last modified: 12.06.2021
# Sources: -
# Description: Prints out CSS ID-selectors for the sudoku game area

# 11 12 13 14 15 16 17 18 19
# 21 22 23 24 25 26 27 28 29
# 31 32 33 34 35 36 37 38 39
# 41 42 43 44 45 46 47 48 49
# - - - -- - - -- -- - -- --
# - - -- - - --- - - - -- -
# 71 72 73 74 75 76 77 78 79
# 81 82 83 84 85 86 87 88 89
# 91 92 93 94 95 96 97 98 99
def print_ids(row_start):
    for row in range(row_start, row_start + 3):
        for col in range(1, 4):
            print("[id=%d%d], " % (row, col), end="")
    for row in range(row_start, row_start + 3):
        for col in range(7, 10):
            print("[id=%d%d], " % (row, col), end="")

print_ids(1)
print_ids(7)

for row in range(4, 7):
    for col in range(4, 7):
        print("[id=%d%d], " % (row, col), end="")
