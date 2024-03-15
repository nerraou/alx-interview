#!/usr/bin/python3
"""n queens puzzle"""
import sys


def is_attacking(queen1, queen2):
    """
    check if a queen is attacking another queen
    """
    if queen1[0] == queen2[0]:
        return True
    if queen1[1] == queen2[1]:
        return True
    if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return True
    return False


def can_put_queen(board, n, queen):
    """
    check if a queen can be put on a square
    """
    for rank in range(n):
        for file in range(n):
            if board[rank][file]:
                if is_attacking(queen, [rank, file]):
                    return False
    return True


def generate_coords(board):
    """
    print queens board
    """
    queens = []

    n = len(board)

    for rank in range(n):
        for file in range(n):
            if board[rank][file]:
                queens.append([rank, file])
    return queens


def solve(n, file, board, result):
    """
    recursive solve
    """
    if file >= n:
        result.append(generate_coords(board))
        return False

    for rank in range(n):
        future_queen = [rank, file]

        if can_put_queen(board, n, future_queen):
            board[rank][file] = True

            if solve(n, file + 1, board, result):
                return True

            board[rank][file] = False

    return False


def n_queens(n):
    """
    solve n queens puzzle
    """
    board = []
    for _1 in range(n):
        rank = []

        for _2 in range(n):
            rank.append(False)

        board.append(rank)

    result = []
    solve(n, 0, board, result)

    result.reverse()
    for b in result:
        print(b)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    n_queens(n)
