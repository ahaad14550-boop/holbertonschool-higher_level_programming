#!/usr/bin/env python3
"""Module that defines a VerboseList that extends the built-in list."""


class VerboseList(list):
    """A custom list class that prints notifications."""

    def append(self, item):
        """Adds an item to the list and prints a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list with multiple items and prints a message."""
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """Removes an item from the list and prints a message first."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a message first."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
