#!/usr/bin/python3
"""In this module the function:
    to_json_string()
    is defined
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
