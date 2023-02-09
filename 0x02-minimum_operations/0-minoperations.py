#!/usr/bin/python3
"""Reimagine the 2 keys keyboard problem.

Perform the prime factorization for the input and
sum the prime factors obtained.
"""


def minOperations(n: int) -> int:
    """Sum the prime factors of the input.

    Args:
        n (int): number to perform prime factorization.
    Return:
        int: sum of the prime factors.
    """
    min_operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            min_operations += factor
            n /= factor
        factor += 1
    return min_operations
