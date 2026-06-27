#!/usr/bin/python3
"""
This module has a Rectangle class that builds on BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle class that uses BaseGeometry to validate its sides.
    """

    def __init__(self, width, height):
        """
        Sets up the rectangle with a width and height after validating them.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
