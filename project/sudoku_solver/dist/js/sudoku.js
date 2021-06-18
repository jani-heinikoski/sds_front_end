/*
Author: Jani Heinikoski
Last modified: 18.06.2021
Description: Sudoku game logic
Sources:*/

/*
1. Load references for the input elements inside the game grid
2. Load references for the sudoku's buttons (solve, reset, load ex.)
3. Register onclicks for the buttons
    3.1 Solve button tries to solve the prefilled sudoku using a backtracking brute force algorithm (refer to docs)
    3.2 Reset button removes all digits from the game grid
    3.3 Load example loads an example sudoku which the algorithm is able to solve fairly efficiently.
*/

// An example sudoku
const EXAMPLE_GAME = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
];

// Checks if the grid has been filled with proper values
function checkGridSanity(gameGrid) {
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            if (gameGrid[i][j].value !== '' && !(gameGrid[i][j].value <= 9 && gameGrid[i][j].value >= 1))
                return false;
        }
    }
    return true;
}

// Fetch the game grid's input elements to a 2D-array
const GAME_GRID = [];
for (i = 1; i < 10; i++) {
    GAME_GRID[i - 1] = [];
    for (j = 1; j < 10; j++) {
        console.log(`${i}${j}`);
        GAME_GRID[i - 1].push(document.getElementById(`${i}${j}`));
    }
}

const SOLVE_BTN = document.getElementsByClassName('solve')[0];
SOLVE_BTN.addEventListener('click', () => {
    console.log(checkGridSanity(GAME_GRID));
});

const RESET_BTN = document.getElementsByClassName('reset')[0];
RESET_BTN.addEventListener('click', () => {
    GAME_GRID.forEach((arr) => {arr.forEach((element) => {element.value = ''})});
})
