#!/usr/bin/python3
"""Module that defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square"""
    def __init__(self, size):
        """Initialize square with given size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
