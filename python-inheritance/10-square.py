#!/usr/bin/python3
"""
This module contains the Square class which inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square using the rectangle class properties.
    """

    def __init__(self, size):
        """
        Initializes the square with a validated size value.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the total area of the square.
        """
        return self.__size ** 2
