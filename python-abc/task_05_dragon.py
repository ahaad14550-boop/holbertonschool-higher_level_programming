#!/usr/bin/env python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin for swimming behavior."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying behavior."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar."""

    def roar(self):
        """Prints a roaring message."""
        print("The dragon roars!")
