#!/usr/bin/python3
"""
The coin Change Algorithm
"""


def makeChange(coins, total):
    """Calculates fewest number needed to meet,
    needed to meet given total amount.
    Args:
        coins ([list]): list of coin values available.
        total ([number]): target amount
    Return: fewest number of coins needed to reach total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    cpy_total = total
    len_coins = len(coins)

    while(i < len_coins and cpy_total > 0):
        if (cpy_total - coins[i]) >= 0:
            cpy_total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = cpy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins
