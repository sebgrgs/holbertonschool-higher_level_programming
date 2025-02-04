#!/usr/bin/env python3
""" FlyingFish class """


class Fish:
    """ Fish class """
    def swim(self):
        """ Fish swim method """
        print("The fish is swimming")

    def habitat(self):
        """ Fish habitat method """
        print("The fish lives in water")


class Bird:
    """ Bird class """
    def fly(self):
        """ Bird fly method """
        print("The bird is flying")

    def habitat(self):
        """ Bird habitat method """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """ FlyingFish class """
    def fly(self):
        """ FlyingFish fly method """
        print("The flying fish is soaring!")

    def swim(self):
        """ FlyingFish swim method """
        print("The flying fish is swimming!")

    def habitat(self):
        """ FlyingFish habitat method """
        print("The flying fish lives both in water and sky!")
