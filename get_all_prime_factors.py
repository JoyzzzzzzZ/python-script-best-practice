#! /usr/bin/env python3

"A module for getting all of the prime factors of an integer."

import sys
from smallest_factor import get_smallest_prime_factor


def get_all_prime_factors(n):
    """

    """
    prime_factor=list()
    a=int(n)
    while a >= 2:
        f=int(smallest_factor.get_smallest_prime_factor(a))
        if f not in prime_factor:
            prime_factor.append(f)
        a=int(a/f)
    return prime_factor

def main():
    import argparse
    from smallest_factor import get_smallest_prime_factor
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")
    
    factors=get_all_prime_factors(n)
    sys.stdout.write('{}\n'.format(factors))
    print('this is main')

if __name__ == '__main__':
    main()

