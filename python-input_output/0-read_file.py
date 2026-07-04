#!/usr/bin/python3
"""
This module has a function that reads a text file.
It opens the file and prints whatever is inside to the screen.
"""


def read_file(filename=""):
    """
    Reads a utf-8 text file and prints its content to stdout.
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
