#!/usr/bin/python3
"""
This module has a function that loads an object from a JSON file.
It reads the file and deserializes the JSON string into a Python object.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
