#!/usr/bin/python3
"""Module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or an instance of a class
    that inherited from the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
