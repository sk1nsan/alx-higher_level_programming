#!/usr/bin/python3
"""append_write function """


def append_write(filename="", text=""):
    """function to append into a file"""
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
