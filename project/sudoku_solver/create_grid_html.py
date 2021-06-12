# Author: Jani Heinikoski
# Last modified: 12.06.2021
# Description:
# Prints out the required inputs for a sudoku game grid 
input_generic = '<input type="number" min="1" max="9" id="%d%d" class="sudoku-cell">'
div_generic = '<div class="row">'
for row in range(1, 10):
    print("<!-- Next row! -->")
    print(div_generic)
    for col in range(1, 10):
        print("\t" + input_generic % (row, col))
    print("</div>")