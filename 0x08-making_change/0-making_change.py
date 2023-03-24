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

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total % coin == 0:
            coin_count += total // coin
            return coin_count
        if total - coin >= 0:
            if total // coin > 1:
                coin_count += total // coin
                total = total % coin
            else:
                coin_count += 1
                total -= coin
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
