#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Executes a function safely"""
    result = 0
    try:
        result = fct(*args)
    except Exception as er:
        stderr.write(f"Exception: {er}\n")
        return None
    return result
