#!/usr/bin/python3
"""In this module the functions lazy_matrix_mul and errors are defined"""
from numpy import matmul

def errors(matrix, name):
    """Checks for erros in matrix"""
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")
    if not matrix or (len(matrix) == 1 and not matrix[0]):
        raise ValueError(f"{name} can't be empty")
    if [k for k in matrix if not isinstance(k, list)]:
        raise TypeError(f"{name} must be a list of lists")
    le = len(matrix[0])
    for i in matrix:
        if [j for j in i if not isinstance(j, (int, float))]:
            raise TypeError(f"{name} should contain only integers or floats")
        if (le != len(i)):
            raise TypeError(f"each row of {name} must be of the same size")
        le = len(i)


def lazy_matrix_mul(m_a, m_b):
    """Return matrix multiplication: m_a . m_b"""

    errors(m_a, "m_a")
    errors(m_b, "m_b")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    return matmul(m_a, m_b)
