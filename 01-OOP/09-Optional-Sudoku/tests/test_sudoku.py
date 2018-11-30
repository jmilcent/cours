import unittest
from sudoku import SudokuSolver

class SudokuSolvertest(unittest.TestCase):
    def test_valid_grid(self):
        grid = [
            [7,8,4,  1,5,9,  3,2,6],
            [5,3,9,  6,7,2,  8,4,1],
            [6,1,2,  4,3,8,  7,5,9],

            [9,2,8,  7,1,5,  4,6,3],
            [3,5,7,  8,4,6,  1,9,2],
            [4,6,1,  9,2,3,  5,8,7],

            [8,7,6,  3,9,4,  2,1,5],
            [2,4,3,  5,6,1,  9,7,8],
            [1,9,5,  2,8,7,  6,3,4]
        ]

        solver = SudokuSolver(grid)
        self.assertTrue(solver.is_valid())


    def test_invalid_grid(self):
        grid = [
            [8,8,4,  1,5,9,  2,2,6],
            [5,2,9,  6,8,2,  8,4,1],
            [6,1,2,  4,2,8,  8,5,9],

            [9,2,8,  8,1,5,  4,6,2],
            [2,5,8,  8,4,6,  1,9,2],
            [4,6,1,  9,2,2,  5,8,8],

            [8,8,6,  2,9,4,  2,1,5],
            [2,4,2,  5,6,1,  9,8,8],
            [1,9,5,  2,8,8,  6,2,4]
        ]

        solver = SudokuSolver(grid)
        self.assertEqual(solver.is_valid(), False)

    def test_invalid_grid2(self):
        grid = [
            [1,2,3, 4,5,6, 7,8,9],
            [2,3,1, 5,6,4, 8,9,7],
            [3,1,2, 6,4,5, 9,7,8],

            [4,5,6, 7,8,9, 1,2,3],
            [5,6,4, 8,9,7, 2,3,1],
            [6,4,5, 9,7,8, 3,1,2],

            [7,8,9, 1,2,3, 4,5,6],
            [8,9,7, 2,3,1, 5,6,4],
            [9,7,8, 3,1,2, 6,4,5]
        ]

        solver = SudokuSolver(grid)
        self.assertEqual(solver.is_valid(), False)
