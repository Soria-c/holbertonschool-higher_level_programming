#!/usr/bin/python3
"""In this module a class Rectangle is defined"""


class Rectangle:
    """Class to create a Rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Method to initialize a new Rectangle object"""
        self.errors(height, "height")
        self.errors(width, "width")

        Rectangle.number_of_instances += 1
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
        self.errors(value, "height")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.errors(value, "width")
        self.__width = value

    def perimeter(self):
        """Instance method that returns the perimeter"""
        if not(self.__height) or not(self.__width):
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def area(self):
        """Instance method that returns the area"""
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Instance method to compare two Rectangle objects"""
        if not(isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not(isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

    def __str__(self):
        """Custom implementation of the __str__ magic method"""
        if not(self.__height) or not(self.__width):
            return ""
        a = [self.__width*str(self.print_symbol) for i in range(self.__height)]
        return "\n".join(a)

    def __repr__(self):
        """Custom implementation of the __str__ magic method"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Custom implementation of the __del__ magic method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def errors(cls, v, name):
        """Class method to check for errors"""
        if not isinstance(v, int):
            raise TypeError(f"{name} must be an integer")
        if v < 0:
            raise ValueError(f"{name} must be >= 0")
