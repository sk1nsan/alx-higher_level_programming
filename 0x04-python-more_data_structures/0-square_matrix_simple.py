#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in matrix:
        m.append(list(map(lambda x: x**2, i)))
    return m
