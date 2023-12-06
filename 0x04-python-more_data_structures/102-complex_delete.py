#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        a = a_dictionary.copy()
        [a_dictionary.pop(x) for x, y in a.items() if y == value]
    return a_dictionary
