#!/usr/bin/python3
"""Module to determine the winner of the prime game."""


def primeNumbers(num):
    """Generates a set of prime numbers.

    Populates the set of prime_numbers upto the limit `num`.
    Args:
        nums (int): upper limit to find prime numbers to.
    """
    if num <= 1:
        return []
    primes = [x for x in range(num + 1)]
    primes[1] = 0
    p = 2
    while p * p <= num:
        if primes[p] != 0:
            for j in range(p*2, num + 1, p):
                primes[j] = 0
        p += 1
    return primes


def isWinner(x, nums):
    """Determine who the winner of the prime game is.

    The loser in each round is determined by who cannot make a move.
    The winner of the game is the individual who won most of the rounds.
    Args:
        x (int): Number of rounds to be played.
        nums (List[int]): Number of n's per round.
    Return:
        string: name of individual who won (either Ben or Maria).
    """
    if x == 0 or nums == []:
        return None
    benCount = mariaCount = 0
    max_number = max(nums)
    game_choices = primeNumbers(max_number)
    for i in range(x):
        round_choices = game_choices[1: nums[i] + 1]
        choices = list(filter(lambda x: x != 0, round_choices))
        if len(choices) % 2 == 0:
            benCount += 1
        else:
            mariaCount += 1
    if benCount > mariaCount:
        return 'Ben'
    elif benCount < mariaCount:
        return 'Maria'
    else:
        None
