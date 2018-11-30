# Sudoku Validator

Congratulations for reaching this exercise! We are going to implement a Sudoku Validator. Its goal is simple: given a Sudoku **9x9 grid**, determine if it is valid!

![](./sudoku.gif)

## Rules

A sudoku is valid if and only if:

- A row must contain all numbers from `1` to `9`
- A column must contain all numbers from `1` to `9`
- Each of the nine 3x3 little squares must contain numbers from `1` to `9`

## Getting started

```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/09-Optional-Sudoku
subl .
```

## Data Model

A Sudoku grid will be represented by a Python list of lists:

```python
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
```

With that structure in mind, you can access a cell at row `i` and column `j` with the following statement:

```python
grid[i][j]
```

💡 Remember that python list indexes start at **`0`**, so `i` and `j` values are between `0` and `8`.

## Exercise

Open the `sudoku.py` file and implement the `is_valid()` instance method of the `SudokuSolver` class. To check if your code is working, you can run the tests with:

```bash
pipenv run nosetests
```

## Done?

We will have a livecode with the whole class very soon. You can practise your Python skill on Codewars (sign in with GitHub!) with the following Kata:

- [Snake and Ladders](https://www.codewars.com/kata/snakes-and-ladders-1/train/python)
- [Decode the morse code](https://www.codewars.com/kata/decode-the-morse-code/train/python)
- [Escape the mines!](https://www.codewars.com/kata/escape-the-mines/train/python)
