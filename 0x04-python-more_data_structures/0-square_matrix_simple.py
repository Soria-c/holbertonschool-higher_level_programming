#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Returns a new 2d array of matrix squared """
    if not isinstance(matrix, list):
        return
    return [[x ** 2 for x in row] for row in matrix]
