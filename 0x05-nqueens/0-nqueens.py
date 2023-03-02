#!/usr/bin/python3
"""N Queens Problem Solver.

This module provides a program that solves the N Queens problem using backtracking. Given an integer N, it tries to place N
non-attacking queens on an NxN chessboard.

Usage:
    python nqueens.py N

where N is an integer greater than or equal to 4.

The program prints every possible solution to the problem, one per line, in the format `(row, col)` for each queen's
position. It doesn't specify a particular order for the solutions.

"""

import sys


def solve_n_queens(n: int) -> list:
    """Solves the N Queens problem and returns a list of solutions.

    Args:
        n: The number of queens and size of the chessboard.

    Returns:
        A list of solutions, where each solution is a list of tuples representing the positions of the queens.

    """
    solutions = []

    def is_valid(board: list, row: int, col: int) -> bool:
        """Checks if a queen can be placed at a given position on the board.

        Args:
            board: The current state of the chessboard.
            row: The row to check.
            col: The column to check.

        Returns:
            True if a queen can be placed at the given position without attacking any other queens on the board,
            False otherwise.

        """
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check diagonal up and left
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check diagonal up and right
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_recursively(board: list, row: int) -> None:
        """Solves the N Queens problem recursively.

        Args:
            board: The current state of the chessboard.
            row: The row to place the next queen on.

        """
        if row == n:
            # All queens have been placed on the board, add solution to the list
            solutions.append([(i, j) for i in range(n) for j in range(n) if board[i][j] == 1])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                solve_recursively(board, row + 1)
                board[row][col] = 0

    # Start solving the problem
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_recursively(board, 0)

    return solutions


if __name__ == '__main__':
    # Parse command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python nqueens.py N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the problem and print solutions
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
