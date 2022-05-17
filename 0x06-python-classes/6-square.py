#!/usr/bin/python3
"""In this module a new class Square is defined"""


class Square:
    """ Class to create an square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of Square
            Args:
                size (int): size of a new Square
        """
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Instance method to calculate the area of a given Square object"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for __size field of a Square object"""
        return self.__size

    @property
    def position(self):
        """Getter method for __position field of a Square object"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method for __size of a Square object"""
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        "Setter method for __position field of a Square object"
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method to print a Square object"""
        if not (self.__size):
            print()
            return
        for i in range(self.__position[1]):
            print()
        s = self.__size
        print("\n".join([" " * self.__position[0]+"#" * s for i in range(s)]))
