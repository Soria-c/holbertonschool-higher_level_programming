#!/usr/bin/python3
"""In this module the function inherits_from is defined"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that it inherited from"""
    return isinstance(obj, a_class) and type(obj) is not a_class
