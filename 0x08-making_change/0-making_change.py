#!/usr/bin/python3
"""Module to determine the fewest number of coins to meet the target."""
import sys


def makeChange(coins, total):
    """Find the fewest number of coins to meet the target.

    Args:
        coins (List[int]): values of the coins in possession.
        total (int): the target value to achieve.
    Return:
        int: number of coins
    """
    if total <= 0:
        return 0
    change = [sys.maxsize] * (total + 1)
    change[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            change[i] = min(change[i], change[i - coin] + 1)
    return change[total] if change[total] != sys.maxsize else -1
