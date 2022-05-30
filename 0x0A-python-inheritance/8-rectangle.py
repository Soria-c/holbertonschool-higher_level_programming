#!/usr/bin/python3
"""In this module the class Rectangle is defined"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to create a new BaseGeometry object, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Implementation of the init magic method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
