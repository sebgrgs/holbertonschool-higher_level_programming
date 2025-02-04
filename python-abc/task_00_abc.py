#!/usr/bin/env python3
""" Task 00: Abstract Base Classes """
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Animal class """
    @abstractmethod
    def sound(self):
        """ Abstract Sound method """
        pass


class Dog(Animal):
    """ Dog class """
    def sound(self):
        """ Dog sound """
        return "Bark"


class Cat(Animal):
    """ Cat class """
    def sound(self):
        """ Cat sound """
        return "Meow"
