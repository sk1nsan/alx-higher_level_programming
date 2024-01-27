#!/usr/bin/python3
"""
    print_square function
    size must be an integer
    size must can't be less than 0

"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
