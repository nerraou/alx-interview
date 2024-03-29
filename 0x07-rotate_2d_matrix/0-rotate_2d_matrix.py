#!/usr/bin/python3
"""rotate 2d matrix
"""


def rotate_2d_matrix(mx):
    """rotate 2d mx in-place
    """
    N = len(mx)

    for y in range(N):
        for x in range(y + 1, N):
            mx[y][x], mx[x][y] = mx[x][y], mx[y][x]

    for y in range(N):
        for x in range(N // 2):
            mx[y][x], mx[y][N - x - 1] = mx[y][N - x - 1], mx[y][x]
