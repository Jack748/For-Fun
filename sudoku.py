def is_valid(puzzle, row, col, num):
    # Check if the number is already present in the same row
    for i in range(9):
        if puzzle[row][i] == num:
            return False
 
    # Check if the number is already present in the same column
    for i in range(9):
        if puzzle[i][col] == num:
            return False
 
    # Check if the number is already present in the same 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False
 
    # If the number is not present in any of the above cases, it is a valid solution
    return True
 
 
def solve_sudoku(puzzle):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                # Try filling the cell with every number from 1 to 9
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        # If the number is valid, fill the cell with it and try to solve the rest of the puzzle
                        puzzle[row][col] = num
                        if solve_sudoku(puzzle):
                            return True
                        # If the puzzle cannot be solved, backtrack and try the next valid number
                        puzzle[row][col] = 0
                # If no valid number can be found for the cell, return False to trigger backtracking
                return False
    # If the puzzle has been completely filled, return True
    return True



import unittest

class TestSudoku(unittest.TestCase):
    def test_is_valid(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        self.assertTrue(solve_sudoku(puzzle))