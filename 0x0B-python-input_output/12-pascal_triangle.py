#!/usr/bin/python3
"""pascal_triangle function"""


def fact(n):
    """function to compute factorial"""
    if n == 0 or n == 1:
        return 1
    return fact(n - 1) * n


def pascal_triangle(n):
    """pascal_triangle function"""

    all_pasacal = []
    if n <= 0:
        return all_pasacal
    for i in range(0, n):
        pascal = []
        for j in range(0, i + 1):
            x = fact(i) / (fact(i - j) * fact(j))
            pascal.append(int(x))
        all_pasacal.append(pascal)
    return all_pasacal
