#!/usr/bin/python3
import json
"""In this module the function:
    save_to_json_file()
    is defined
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
