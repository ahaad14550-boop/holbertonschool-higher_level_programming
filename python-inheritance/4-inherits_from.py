#!/usr/bin/python3
"""
This file has a function to check subclass inheritance for an object.
"""


def inherits_from(obj, a_class):
    """
    This function checks if the object is an inherited instance of a class,
    but ensures it is not exactly the same class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
