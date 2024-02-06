#!/usr/bin/python3
"""json module"""
import json


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string)"""
    return json.loads(my_str)
