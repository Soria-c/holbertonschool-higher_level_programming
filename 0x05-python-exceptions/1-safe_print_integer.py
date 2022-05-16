#!/usr/bin/python3
def safe_print_integer(value):
    """Checks for Value Error exception"""
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
