#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns new dict with values of a_dictionary multiplied by 2"""
    if not isinstance(a_dictionary, dict):
        return
    return {k: v * 2 for (k, v) in a_dictionary.items()}
