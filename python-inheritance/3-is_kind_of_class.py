#!/usr/bin/python3
"""
This file has a function that checks the class type of an object.
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object belongs to the class
    or if it belongs to a class that inherits it.
    """
    return isinstance(obj, a_class)
