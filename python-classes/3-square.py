#!/usr/bin/python3
"""Module that defines a Square classe"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize square with given size
        Args:
            size: size of the square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns The area of the square"""
        return self.__size ** 2
