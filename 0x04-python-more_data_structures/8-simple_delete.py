#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Returns a_dictionary excluding the value of key"""
    if not isinstance(a_dictionary, dict):
        return
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
