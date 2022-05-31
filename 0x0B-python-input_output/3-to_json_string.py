#!/usr/bin/python3
import json
"""In this module the function:
    to_json_string()
    is defined
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
