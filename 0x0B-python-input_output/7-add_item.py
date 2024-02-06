#!/usr/bin/python3
"""json module"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args_list = sys.argv[1:]
if os.path.isfile("add_item.json"):
    l = load_from_json_file("add_item.json")
    l.extend(args_list)
    save_to_json_file(l, "add_item.json")
else:
    save_to_json_file(args_list, "add_item.json")
