#!/usr/bin/python3
"""In this module the functions errors() and add_integer() are defined"""


def matrix_divided(matrix, div):
    """Returns a new 2d list of matrix / 2"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(m)
    if [k for k in matrix if not isinstance(k, list)]:
        raise TypeError(m)
    le = len(matrix[0])
    for i in matrix:
        if [j for j in i if not isinstance(j, (int, float))]:
            raise TypeError(m)
        if (le != len(i)):
            raise TypeError("Each row of the matrix must have the same size")
        le = len(i)

    return list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))
