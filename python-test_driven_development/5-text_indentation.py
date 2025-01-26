#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters:
    ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            if c + 1 < len(text):
                while c + 1 < len(text) and text[c + 1] == ' ':
                    c += 1
        c += 1
