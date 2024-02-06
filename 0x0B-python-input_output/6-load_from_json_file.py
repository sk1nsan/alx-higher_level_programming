#!/usr/bin/python3
"""json module"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="UTF8") as f:
        return json.loads(f.read())
