#!/usr/bin/python3
"""In this module the function:
    read_file()
    is defined
"""


def read_file(filename=""):
    """Opens a file, reads it, and prints its contents"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
