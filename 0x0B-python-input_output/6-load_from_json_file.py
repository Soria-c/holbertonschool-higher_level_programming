#!/usr/bin/python3
import json
"""In this module the function:
    load_from_json_file()
    is defined
"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file.read())
