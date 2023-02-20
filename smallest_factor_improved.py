#! /usr/bin/env python3

"A module for getting the smallest prime factor of an integer."

import sys



def get_smallest_prime_factor(n):
    """
    Returns the smallest integer that is a factor of `n`.

    if `n` is a prime number `n` itself is returned.

    Parameters
    ----------
    n : int
        The interger to be factored

    Returns
    -------
    int

    Examples
    --------
    >>> get_smallest_prime_factor(7)
    >>> get_smallest_prime_factor(8)
    2
    >>> get_smallest_prime_factor(9)
    3
    """
    for i in range(2, n+1):
        if (n % i) == 0:
            return i

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    print(get_smallest_prime_factor(n))
