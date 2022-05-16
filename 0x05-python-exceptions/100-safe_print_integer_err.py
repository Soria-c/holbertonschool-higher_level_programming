#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """Prints an integer, checks for exceptions"""
    try:
        print("{:d}".format(value))
    except Exception as er:
        stderr.write(f"Exception: {er}\n")
        return False
    return True
