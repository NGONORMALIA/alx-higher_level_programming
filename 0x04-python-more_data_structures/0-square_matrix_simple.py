#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if len(matrix) == 0 or matrix is None:
        return (None)
    for row in matrix:
        new.append(list(map(lambda x: x ** 2, row)))
    return new
