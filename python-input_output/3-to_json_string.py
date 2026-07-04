#!/usr/bin/python3
"""
This module has a function that converts an object to JSON.
It uses the built-in json module to return a string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.
    """
    return json.dumps(my_obj)
