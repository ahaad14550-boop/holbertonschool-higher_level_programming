#!/usr/bin/python3
"""
This module contains the Square class version 2 which inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square and handles its size and printing.
    """

    def __init__(self, size):
        """
        Initializes the square with validation using the rectangle format.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the total area of the square instance.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the customized printable string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
