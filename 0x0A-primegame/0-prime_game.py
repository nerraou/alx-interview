#!/usr/bin/python3
"""prime game module"""


def sieve_of_eratosthenes(n):
    """return list of prime numbers less then or equal to n
    """
    prime = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)

    return prime_numbers


def count_primes(primes_list, n):
    """count prime numbers less then or equal to n
    """
    count = 0
    for prime in primes_list:
        if prime > n:
            return count
        count += 1

    return count


def isWinner(x, nums):
    """isWinner function
    """

    if x == 0:
        return None

    max_number = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_number)
    maria_wins = 0
    ben_wins = 0

    for i in range(0, x):
        n = nums[i]
        count = count_primes(prime_numbers, n)

        if count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    return None
