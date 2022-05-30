#!/usr/bin/python3
"""In this module the function add_attribute is defined"""


def add_attribute(obj, var, value):
    """Checks if an acttribute can be added to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, var, value)
