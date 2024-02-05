#!/usr/bin/python3
""" BaseGeometry  """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Rectangle init function"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Rectangle area function"""

        return self.__width * self.__height

    def __str__(self):
        """Rectangle when printed"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
