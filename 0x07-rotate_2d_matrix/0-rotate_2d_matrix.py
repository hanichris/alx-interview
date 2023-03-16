#!/usr/bin/python3
"""Rotate a 2 dimensional matrix 90 degrees clockwise."""


def rotate_2d_matrix(matrix) -> None:
    """Perfoms a 90 degree clockwise rotation of the matrix.

    The rotation is done in place.
    Args:
        matrix (List[List]): non-empty 2D matrix.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
