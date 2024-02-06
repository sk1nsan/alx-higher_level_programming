#!/usr/bin/python3
""" add_attribute function  """


def add_attribute(class_name, attribute_name, value):
    """add_attribute function"""
    if attribute_name in globals():
        raise TypeError("can't add new attribute")
    if class_name not in globals():
        raise TypeError("can't add new attribute")
    setattr(class_name, attribute_name, value)
