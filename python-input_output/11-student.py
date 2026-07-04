#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization.
It provides methods to convert class instances to JSON dictionaries and
reload attributes back from a JSON dictionary.
"""


class Student:
    """
    Represents a student entity with first name, last name, and age.
    This class handles basic student data and its dictionary representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the required personal details.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are included
        in the final returned dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all public attributes of the Student instance dynamically
        using the key-value pairs provided in the input json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
