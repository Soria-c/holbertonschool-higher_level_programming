#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns number of keys of a_dictionary"""
    if not isinstance(a_dictionary, dict):
        return
    return len(a_dictionary)
