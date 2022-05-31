#!/usr/bin/python3
"""In this module the function:
    write_file()
    is defined
"""


def write_file(filename="", text=""):
    """Creates or writes/overwrites a text in to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
