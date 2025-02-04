#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Shape(ABC):
    """ Shape class """
    @abstractmethod
    def area(self):
        """ Abstract area method """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract perimeter method """
        pass


class Circle(Shape):
    """ Circle class """
    def __init__(self, radius):
        """ Circle constructor """
        self.radius = radius

    def area(self):
        """ Circle area """
        return 3.141592653589793 * self.radius ** 2

    def perimeter(self):
        """ Circle perimeter """
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Rectangle constructor """
        self.width = width
        self.height = height

    def area(self):
        """ Rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Rectangle perimeter """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ Shape information """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
