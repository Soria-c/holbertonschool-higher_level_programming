#!/usr/bin/python3
"""In this module a new class Square is defined"""


class Square:
    """ Class to create an square object"""
    def __init__(self, size=0):
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Instance method to calculate the area of a given Square object"""
        return self.__size ** 2
