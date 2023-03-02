#!/usr/bin/python3
"""Solves the N-queen puzzle.

Determines all the possible solutions to placing N
non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater or equal to 4
Attributes:
    board (list(list)): A matrix representing the chessboard.
    solutions (list(list)):  A new matrix holding the solution.
Solutions are represented in the format [[r, c]...] where `r`
and `c` represent the row and column where the queen can be
placed on the chessboard.
"""
import sys


def is_safe(board, row, col):
    """Determines if board[row][col] can hold a queen.

    Checks the left-diagonals of the particular cell and the
    left-hand side of the cell on the same row.
    Args:
        board (list(list)): matrix representing chessboard.
        row (int): row index of the chessboard.
        col (int): column index of the chessboard.
    """
    for index in range(col):
        if board[row][index]:
            return False

    i_row = row
    j_col = col
    while i_row >= 0 and j_col >= 0:
        if board[i_row][j_col]:
            return False
        i_row -= 1
        j_col -= 1
    i_row = row
    j_col = col
    while i_row < len(board) and j_col >= 0:
        if board[i_row][j_col]:
            return False
        i_row += 1
        j_col -= 1
    return True


def solve_NQ_util(board, column):
    """Recursive utility function to solve N queen puzzle.

    Args:
        board (list(list)): matrix representing chessboard.
        column (int): column index of the chessboard.
    """
    if column == len(board):
        solution = []
        N = len(board)
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True

    res = False
    for row_index in range(len(board)):
        if is_safe(board, row_index, column):
            board[row_index][column] = 1
            res = solve_NQ_util(board, column + 1) or False
            board[row_index][column] = 0
    return res


def solve_NQ(N):
    """Solve the N queen puzzle using backtracking.

    Uses solve_NQ_util() to solve the problem. Returns False if
    queens cannot be placed otherwise returns True. Prints the
    placement of queens in terms of the board indices.
    Args:
        N (int): The number of queens to be placed. It is equal to
            the size of the chessboard.
    """
    board = [[0 for col in range(N)] for row in range(N)]
    solve_NQ_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except TypeError:
        pass
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    else:
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

    solve_NQ(n)
