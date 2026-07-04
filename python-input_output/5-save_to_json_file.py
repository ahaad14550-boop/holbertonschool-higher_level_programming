#!/usr/bin/python3
"""
This module has a function that saves an object to a file.
It serializes the object to JSON format and writes it.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
