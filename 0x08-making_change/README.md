# Making Change
## Description
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total. The function prototype is:
```def makeChange(coins, total)``` where ``coins`` is a list of the values of the coins in one's possession. The value of a coin is always greater than 0.
The function returns:
* The fewest number of coins needed to meet the total.
* if the total is ``0`` or less, return ``0``.
* if the total cannot be met by any number of coins you have, return ``-1``.