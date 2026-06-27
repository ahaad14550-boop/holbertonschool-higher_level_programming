#!/usr/bin/env python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """A class that counts items during iteration."""

    def __init__(self, iterable):
        """Initializes the iterator and counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the item count."""
        return self.counter

    def __next__(self):
        """Fetches next item and increments counter."""
        item = next(self.iterator)
        self.counter += 1
        return item
