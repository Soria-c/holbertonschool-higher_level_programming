#!/usr/bin/python3
"""In this module the class Square is defined"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """Implementation of the __init__ magic method"""
        super().integer_validator("size", size)
        super().__init__(size, size)
