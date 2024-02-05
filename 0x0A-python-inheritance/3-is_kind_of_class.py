#!/usr/bin/python3
""" is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function"""
    return isinstance(obj, a_class) or obj.__class__ == a_class
