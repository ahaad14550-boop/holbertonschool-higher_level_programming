#!/usr/bin/env python3
"""
This module contains functions for basic data serialization.
It helps save a dictionary to a JSON file and load it back.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Converts a Python dictionary to JSON format and saves it to a file.
    If the file is already there, it will overwrite it.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Opens a JSON file and converts its contents back into a Python dictionary.
    Returns the loaded dictionary data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
