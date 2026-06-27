#!/usr/bin/python3
"""
This module defines the abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing a generic animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all animal subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass representing a dog.
    """

    def sound(self):
        """
        Returns the specific sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass representing a cat.
    """

    def sound(self):
        """
        Returns the specific sound of a cat.
        """
        return "Meow"
