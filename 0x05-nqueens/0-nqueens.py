#!/usr/bin/python3
"""Solves the N-queen puzzle.

Determines all the possible solutions to placing N
non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater or equal to 4
Attributes:
    board (List): A row vector representing the chessboard.
    solutions (list(list)):  A new matrix holding the solution.
Solutions are represented in the format [[r, c]...] where `r`
and `c` represent the row and column where the queen can be
placed on the chessboard.
"""
import sys


def is_safe(columns, row, col):
    """Test whether a given index is viable to place a queen.

    Test performs verticality test and diagonal test to check
    the suitability of column index in a given row.
    Args:
        columns (List): row vector of column indexes.
        row (int): row index.
        col (int): column index.
    Return:
        bool: A measure of the suitability of the column index.
    """
    for _r in range(row):
        _c = columns[_r]
        if _c == col:
            return False
        row_dist = row - _r
        col_dist = abs(col - _c)
        if row_dist == col_dist:
            return False
    return True


def solve_nq(columns, row_index, nqueens):
    """Solve the n queens puzzle using backtracking.

    Args:
        columns (list): row vector representing the chessboard.
        row_index (int): row index of the chessboard.
        nqueens (int): number of queens to place on the chessboard.
    """
    if row_index == nqueens:
        soln = []
        for i in range(nqueens):
            soln.append([i, columns[i]])
        print(soln)
        return
    for col in range(nqueens):
        if is_safe(columns, row_index, col):
            columns[row_index] = col
            solve_nq(columns, row_index + 1, nqueens)


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

    columns = [-1] * n
    solve_nq(columns, 0, n)
