#!/usr/bin/python3
"""In this module a class Rectangle is defined"""


class Rectangle:
    """Class to create a Rectangle object"""

    def __init__(self, width=0, height=0):
        """Method to initialize a new Rectangle object"""
        self.error_h(height)
        self.error_w(width)

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.error_h(value)
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.error_w(value)
        self.__width = value

    @classmethod
    def error_w(cls, w):
        """Class method to check for errors"""
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")

    @classmethod
    def error_h(cls, h):
        """Class method to check for errors"""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
