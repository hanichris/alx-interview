#!/usr/bin/python3
"""Compute the perimeter of the island in the grid."""


def island_perimeter(grid) -> int:
    """Computes the perimeter of the island within the grid.

    Args:
        grid (List[List[int]]): list of list of integers.
    Return:
        int: island perimeter.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                cell_perimeter = 4
                if row > 0:
                    cell_perimeter -= grid[row - 1][col]
                if row < rows - 1:
                    cell_perimeter -= grid[row + 1][col]
                if col < cols - 1:
                    cell_perimeter -= grid[row][col + 1]
                if col > 0:
                    cell_perimeter -= grid[row][col - 1]
                perimeter += cell_perimeter
    return perimeter
