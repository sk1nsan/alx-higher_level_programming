#!/usr/bin/python3
""" Base class """
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        height = self.__height
        width = self.__width
        x = self.__x
        y = self.__y
        print("\n" * y, end="")
        [print(" " * x + "#" * width) for i in range(height)]

    def __str__(self):
        """string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/" "{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """update values of rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """return dict representation of an object"""
        attrs = ["id", "width", "height", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
