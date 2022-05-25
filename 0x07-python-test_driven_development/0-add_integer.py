#!/usr/bin/python3
"""In this module the functions errors() and add_integer() are defined"""


def errors(value, name):
    """Handles errors from add_integer()"""
    if not isinstance(value, int) and not isinstance(value, float):
        raise TypeError(f"{name} must be an integer")


def add_integer(a, b=98):
    """Returns the sum between a and b"""
    errors(a, "a")
    errors(b, "b")
    return int(a) + int(b)
