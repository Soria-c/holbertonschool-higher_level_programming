#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns symmetric difference between set_1 and set_2"""
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return
    return set_1.symmetric_difference(set_2)
