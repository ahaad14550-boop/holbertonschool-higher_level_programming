#!/usr/bin/env python3
"""
This module defines a custom Python class called CustomObject.
It includes methods for binary serialization and deserialization
using Python's built-in pickle module with exception handling.
"""
import pickle


class CustomObject:
    """
    A class that represents a custom object with personal details.
    Provides methods to display, serialize, and deserialize its data.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new instance of CustomObject with basic attributes.
        This constructor sets up the initial values for the instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in the exact expected format.
        Each attribute is displayed on a separate line for clarity.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current object instance into binary format
        and saves it to the given file. Returns None if it fails.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized CustomObject from a binary file and
        returns the instance. Returns None if the file has issues.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
