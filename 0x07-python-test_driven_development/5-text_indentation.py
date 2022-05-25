#!/usr/bin/python3
"""In this module the function text_indentation() is defined"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in ".:?":
        text = f"{x}\n\n".join([i.strip() for i in text.split(x)])
    print(text,end="")