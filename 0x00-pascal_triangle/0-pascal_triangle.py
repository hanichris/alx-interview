#!/usr/bin/python3
"""Compute the coefficients of Pascal's triangle."""


def pascal_triangle(n):
    """Returns list of lists of integers representing Pascal's triangle.

    The entries in the list of list are computed using binomial expansion.
    Args:
        n (int): number of rows in the triangle.

    Return:
        list of lists.
    """
    result = []

    if type(n) is not int or n <= 0:
        return result

    for row in range(n):
        temp = []
        for j in range(row + 1):
            # _x = int(temp[j-1] * ((Decimal(row - j + 1)) / Decimal(j)))
            if j == 0 or j == row:
                temp.append(1)
            elif row > 0 and j > 0:
                temp.append(result[row - 1][j - 1] + result[row - 1][j])
        result.append(temp)
    return result
