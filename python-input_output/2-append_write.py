#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file and returns the number of char"""

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
