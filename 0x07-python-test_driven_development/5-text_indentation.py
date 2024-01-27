#!/usr/bin/python3
"""
    text_indentation function
    text must be a string
    raise TypeError otherwise

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        print(c, end="")
        if c in ['.', '?', ':']:

            print('\n')
