#!/usr/bin/python3
"""In this module a new class Square is defined"""


class Square:
    """ Class to create an square object"""
    def __init__(self, size=0):
        """Initializes a new instance of Square
            Args:
                size (int): size of a new Square
        """
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Instance method to calculate the area of a given Square object"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for a Square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for a Square object"""
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, square2):
        """Implementation of __lt__ magic method"""
        if (self.__size < square2.__size):
            return True
        return False

    def __le__(self, square2):
        """Implementation of __le__ magic method"""
        if (self.__size <= square2.__size):
            return True
        return False

    def __eq__(self, square2):
        """Implementation of __eq__ magic method"""
        if (self.__size == square2.__size):
            return True
        return False

    def __gt__(self, square2):
        """Implementation of __gt__ magic method"""
        if (self.__size > square2.__size):
            return True
        return False

    def __ge__(self, square2):
        """Implementation of __ge__ magic method"""
        if (self.__size >= square2.__size):
            return True
        return False
