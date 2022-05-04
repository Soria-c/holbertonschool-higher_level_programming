#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Return a sum of all unique numbers in my_list"""
    if not isinstance(my_list, list):
        return
    return sum(set(my_list))
