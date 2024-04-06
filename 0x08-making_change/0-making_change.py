#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    check = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            tmp += 1
        if check == total:
            return tmp
        check -= 1
        tmp -= 1
    return -1
