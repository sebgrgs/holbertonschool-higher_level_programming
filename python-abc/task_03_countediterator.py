#!/usr/bin/env python3


class CountedIterator:
    """An iterator that counts the number of elements iterated over."""
    def __init__(self, iterable):
        """Initialize the iterator with the given iterable."""
        self.iterable = iter(iterable)
        self.counter = 0

    def get_count(self):
        """ Return the number of elements iterated over. """
        return self.counter

    def __next__(self):
        """ Return the next element from the iterable. """
        item = next(self.iterable)
        self.counter += 1
        return item
