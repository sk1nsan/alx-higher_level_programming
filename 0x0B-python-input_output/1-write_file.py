#!/usr/bin/python3
"""write_file function """


def write_file(filename="", text=""):
    """function to write into a file"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
