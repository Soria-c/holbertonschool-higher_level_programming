#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Returns sorts and prints elements in a_dictionary"""
    if not isinstance(a_dictionary, dict):
        return
    for i in sorted(a_dictionary):
        print(f"{i}: {a_dictionary[i]}")
