#!/usr/bin/python3
"""In this module the function:
    fromm_json_string()
    is defined
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON str"""
    return json.loads(my_str)
