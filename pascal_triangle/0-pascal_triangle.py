#!/usr/bin/python3
"""This module provides a function to generate a
Pascal's Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates and returns Pascal's Triangle up to
    n rows as a list of lists. Returns an empty list
    if n is less than or equal to 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
