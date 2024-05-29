#!/usr/bin/python3
"""
   Description: N queens puzzle is challenge of placing N non-attacking
                queens on N×N chessboard. Write program that solves N
                queens problem.
   Usage: nqueens N:
          If user called program with wrong number of arguments,
          print Usage: nqueens N, followed by new line, and exit with
          status 1
   where N must be integer greater or equal to 4:
          If N is not integer, print N must be number, followed by new
          line, and exit with status 1
          If N is smaller than 4, print N must be at least 4, followed by new
          line, and exit with status 1
   program should print every possible solution to problem:
          One solution per line
          Format: see example
          You don’t have to print solutions in specific order
   You are only allowed to import sys module
"""


import sys


def print_board(board):
    """ The print_board
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, col, number):
    """ The isSafe
    Args:
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing movement in this position
        col - col to check if is safe doing movement in this position
        number: size of board
    Return: True of False
    """

    # Check row in left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # This Checks upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, number, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, number):
    """ The use of an auxiliary method to explore all possible answers.
    Args:
        board - Board to resolve
        col - Number of col
        number - size of board
    Returns:
        All posibilites to solve problem
    """

    if (col == number):
        print_board(board)
        return True
    res = False
    for i in range(number):

        if (isSafe(board, i, col, number)):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # It Makes result true if any placement
            # is possible
            res = solveNQUtil(board, col + 1, number) or res

            board[i][col] = 0  # BACKTRACK

    return res


def solve(number):
    """ Find all posibilities if exists
    Args:
        number - size of board
    """
    board = [[0 for i in range(number)]for i in range(number)]

    if not solveNQUtil(board, 0, number):
        return False

    return True


def validate(args):
    """ Validate input data to verify if size to
        answer is posible
    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        # Validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Main method to execute application
    """

    number = validate(sys.argv)
    solve(number)
