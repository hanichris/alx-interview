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

    if n <= 0:
        return result

    for row in range(n):
        temp = [1]
        for j in range(1, row + 1):
            _x = int(temp[j-1] * ((row - j + 1) / j))
            temp.append(_x)
        result.append(temp)
    return result
