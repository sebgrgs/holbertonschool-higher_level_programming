#!/usr/bin/python3
"""Module for student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict
