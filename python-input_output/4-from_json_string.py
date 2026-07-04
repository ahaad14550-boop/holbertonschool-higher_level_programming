#!/usr/bin/python3
"""
This module has a function that converts a JSON string to an object.
It deserializes the string back into Python data structures.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.
    """
    return json.loads(my_str)
