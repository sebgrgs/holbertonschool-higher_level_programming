#!/usr/bin/env python3
""" VerboseList class """


class VerboseList(list):
    """ VerboseList class """
    def append(self, item):
        """ Append method """
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, number):
        """ Extend method """
        print("Extented the list with [{}] items.".format(len(number)))
        super().extend(number)

    def remove(self, item):
        """ Remove method """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """ Pop method """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
