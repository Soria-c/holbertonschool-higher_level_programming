#!/usr/bin/python3
"""In this module the function is_same_class is defined"""


def is_same_class(obj, a_class):
    """Chacks if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
