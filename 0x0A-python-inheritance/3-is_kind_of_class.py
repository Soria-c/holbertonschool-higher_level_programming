#!/usr/bin/python3
"""In this module the function is_kind_of_class is defined"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance following the inheritance chain"""
    return isinstance(obj, a_class)
