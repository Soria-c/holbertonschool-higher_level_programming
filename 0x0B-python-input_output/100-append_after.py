#!/usr/bin/python3
"""
This module defines the functions:
    append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a string after each line containing a specific string"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        txt = "".join([i + new_string if search_string in i else i for i in f])
        f.seek(0)
        f.write(txt)
