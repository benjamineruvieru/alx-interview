#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    '''finds no of time opertion is performed
    '''
    if not isinstance(n, int):
        return 0
    letter = 'H'
    count = 0
    pad = ''
    while len(letter) < n:
        if n % len(letter) != 0:
            letter += pad
            count += 1
        else:
            pad = letter
            letter += pad
            count += 2
    return (count if len(letter) == n else 0)

