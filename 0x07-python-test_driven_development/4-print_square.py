#!/usr/bin/python3
"""In this module the functions print_square() are defined"""


def print_square(size):
    """Prints a square of size=size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not size:
        return
    print("\n".join(["#" * size for i in range(size)]))
