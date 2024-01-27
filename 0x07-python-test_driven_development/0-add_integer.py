#!/usr/bin/python3
"""
    add function
    must be an integer or float raises TypeError otherwise
    a, b are converted into ints before adding
"""


def add_integer(a, b=98):
    """
    Return a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
