#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle using BaseGeometry validation.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the official string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
