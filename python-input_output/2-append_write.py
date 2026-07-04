#!/usr/bin/python3
"""
This module has a function that appends text to a file.
It returns the number of characters successfully added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
