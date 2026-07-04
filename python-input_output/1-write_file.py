#!/usr/bin/python3
"""
This module has a function that writes text to a file.
It returns the total number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns character count.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
