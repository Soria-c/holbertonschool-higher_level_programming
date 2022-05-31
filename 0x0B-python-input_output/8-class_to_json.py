#!/usr/bin/python3
"""
In this module the function:
    class_to_json()
    is defined
"""


def class_to_json(obj):
    """Returns of all attributes of an object"""
    return obj.__dict__
