#!/usr/bin/python3
"""In this module the functions matrix_mul and errors are defined"""


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


def matrix_mul(m_a, m_b):
    """Prints a text with 2 new lines after each of these characters . ? :"""

    errors(m_a, "m_a")
    errors(m_b, "m_b")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        re = []
        for j in range(len(m_b[0])):
            r = 0
            for k in range(len(m_a[0])):
                r += (m_a[i][k] * m_b[k][j])
            re.append(r)
        result.append(re)
    return result
