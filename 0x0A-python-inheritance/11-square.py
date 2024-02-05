#!/usr/bin/python3
""" Rectangle  """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Square init function"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square area function"""

        return self.__size * self.__size

    def __str__(self):
        """Square when printed"""
        return "[Square] {}/{}".format(self.__size, self.__size)
