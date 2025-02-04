#!/usr/bin/env python3
""""Module for the Dragon class."""


class SwimMixin:
    """Mixin class for the swim method."""
    def swim(self):
        """Method for the swim action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class for the fly method."""
    def fly(self):
        """Method for the fly action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""
    def roar(self):
        """Method for the roar action."""
        print("The dragon roars!")
