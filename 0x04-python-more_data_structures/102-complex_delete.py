#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return
    for k, v in dict(a_dictionary).items():
        if (v == value):
            del a_dictionary[k]
    return a_dictionary
