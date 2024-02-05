#!/usr/bin/python3
""" inherits_from function """


def inherits_from(obj, a_class):
    """inherits_from function"""
    return isinstance(obj, a_class) and not obj.__class__ == a_class
