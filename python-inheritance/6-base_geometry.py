#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """Class that defines a base geometry"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")
