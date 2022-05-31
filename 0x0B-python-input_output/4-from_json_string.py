#!/usr/bin/python3
import json
"""In this module the function:
    fromm_json_string()
    is defined
"""


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)
