#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result"""
    c = 0
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print(f"Inside result: {c}")
    return c
