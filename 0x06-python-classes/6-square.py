#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        x, y = self.__position
        print("\n" * y, end="")
        [print(" " * x + "#" * self.__size) for i in range(self.__size)]
        if self.__size == 0:
            print()
