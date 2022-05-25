#!/usr/bin/python3
"""In this module the functions errors() and sat_my_name() are defined"""


def errors(v, name):
    """Checks for TypeError"""
    if not isinstance(v, str):
        raise TypeError(f"{name} must be a string")


def say_my_name(first_name, last_name=""):
    """Prints a formated string"""
    errors(first_name, "first_name")
    errors(last_name, "last_name")

    print(f"My name is {first_name} {last_name}")
