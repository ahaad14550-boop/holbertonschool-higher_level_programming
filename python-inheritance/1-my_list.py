#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """A custom list class that adds sorted functionality."""

    def print_sorted(self):
        """Prints the elements of the list sorted ascendingly."""
        print(sorted(self))
