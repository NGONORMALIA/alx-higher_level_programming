#!/usr/bin/python3
"""
Module to divide all element in a matrix by a given integer
"""


def matrix_divided(matrix, div):
    """to dive all element in a matrix

    Args:
        matrix: the matrix to divide all its element
        div: the divider

    Raises:
        typeError: if matrix is not a list of list
        of integer or div is not a number
        ZerodivisionError: if div is equal to 0

    return:
         the new matrix with all element divided by div
    """
    d = len(matrix[0])
    new = []
    if (not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(num, list) for num in matrix)
        or not all((isinstance(elem, int))
                   or (isinstance(elem, float))
                   for elem in [a for b in matrix for a in b])):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not (all(len(a) == len(matrix[0]) for a in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for line in matrix:
        rows = []
        for item in line:
            rows.append(round(item / div, 2))
        new.append(rows)
    return new
