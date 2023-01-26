#!/usr/bin/python3
"""
Pascal Trangle
"


def pascal_triangle(n):
    '''
    Creates a list of lists of integers in a Pascal's triangle
    of a given integer.
    '''
    if n <= 0:
        return []
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
