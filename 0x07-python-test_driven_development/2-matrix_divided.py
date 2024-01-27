#!/usr/bin/python3
"""
    matrix_divided function
    div must be an integer or float raise and it can't be zero
    matrix elements must be an integer or float and row size must be constant
"""


def matrix_divided(matrix, div):
    """
    Return a copy of matrix divided by div
    """
    flag = 1

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [[i for i in row] for row in matrix]
    for i in range(len(matrix)):
        if flag == 1:
            rowlen = len(matrix[i])
            flag = 0
        if rowlen != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            newmatrix[i][j] = round(matrix[i][j]/div, 2)
    return newmatrix
