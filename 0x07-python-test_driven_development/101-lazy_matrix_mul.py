#!/usr/bin/python3
"""In this module the functions lazy_matrix_mul and errors are defined"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Return matrix multiplication: m_a ."""
    return matmul(m_a, m_b)
