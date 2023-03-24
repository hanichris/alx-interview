#!/usr/bin/python3
"""Module to determine the fewest number of coins to meet the target."""
from functools import lru_cache


def makeChange(coins, total):
    """Find the fewest number of coins to meet the target.

    Args:
        coins (List[int]): values of the coins in possession.
        total (int): the target value to achieve.
    Return:
        int: number of coins
    """
    @lru_cache(None)
    def dfs(rem):
        if rem <= 0:
            return 0
        min_cost = float('inf')
        for coin in coins:
            res = dfs(rem - coin)
            if res != -1:
                min_cost = min(min_cost, res + 1)
        return min_cost if min_cost != float('inf') else -1
    return dfs(total)
