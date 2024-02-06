#!/usr/bin/python3
"""json module"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(json.dumps(my_obj))
