#!/usr/bin/python3
"""Module for matrix division.

This module provides a function `matrix_divided` that divides all elements
of a matrix by a given number, rounding the results to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not of the same size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix with all elements divided by div.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
