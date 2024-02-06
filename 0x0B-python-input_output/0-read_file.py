#!/usr/bin/python3
"""read_file function """


def read_file(filename=""):
    """function to read file"""
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read())
