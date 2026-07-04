#!/usr/bin/python3
"""
This module has a function that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
