#!/usr/bin/python3
"""In this module the function add_attribute is defined"""


def add_attribute(obj, var, value):
    """Checks if an acttribute can be added to an object"""
    if not "__dict__" in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__setattr__(var, value)
