#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """generate pascal triangle"""
    if (n <= 0):
        return []

    matrix = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            a = matrix[i - 1][j - 1]
            b = matrix[i - 1][j]
            row.append(a + b)
        row.append(1)
        matrix.append(row)

    return matrix
