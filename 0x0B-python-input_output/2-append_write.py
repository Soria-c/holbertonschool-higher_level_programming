#!/usr/bin/python3
"""In this module the function:
    append_write()
    is defined
"""


def append_write(filename="", text=""):
    """Creates or appends a text in to a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
