#!/usr/bin/python3
"""This module defines that class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class to create a new Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Implementation of the __init__ magic method"""
        Rectangle.error_check(**{
            "width": width,
            "height": height,
            "x": x,
            "y": y
            })
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """Recturns the area of a shape"""
        return self.__width * self.__height

    def display(self):
        """Display the shape en stdout"""
        for i in range(self.__y):
            print()
        h = self.__height
        w = self.__width
        print("\n".join([" " * self.__x+"#" * w for i in range(h)]))

    def update(self, *args, **kwargs):
        """Updates the attributes of an object"""
        cl = self.__class__.__name__
        larg = len(args)
        if (cl == "Square"):
            k = ["id", "size", "x", "y"]
            if larg > 4:
                larg = 4
        elif (cl == "Rectangle"):
            k = ["id", "width", "height", "x", "y"]
            if larg > 5:
                larg = 5
        if args and args[0]:
            for i in range(larg):
                setattr(self, k[i], args[i])
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dictionary representation of an object"""
        c = self.__class__.__name__
        if (c == "Square"):
            return {"id": self.id, "size": self.width, "x": self.x,
                    "y": self.y}
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """Custom implementation of the __str__ magic method"""
        cl = self.__class__.__name__
        msg = f"[{cl}] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
        if (cl == "Square"):
            return msg
        return msg + f"/{self.__height}"

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        Rectangle.error_check(**{"width": value})
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        Rectangle.error_check(**{"height": value})
        self.__height = value

    @property
    def x(self):
        """x coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x coordinate setter"""
        Rectangle.error_check(**{"x": value})
        self.__x = value

    @property
    def y(self):
        """y coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y coordinate setter"""
        Rectangle.error_check(**{"y": value})
        self.__y = value

    @classmethod
    def error_check(cls, **values):
        """Checks for invalid inputs"""
        for k, v in values.items():
            if type(v) is not int:
                raise TypeError(f"{k} must be an integer")
            if v <= 0 and k in ["height", "width"]:
                raise ValueError(f"{k} must be > 0")
            if v < 0:
                raise ValueError(f"{k} must be >= 0")
