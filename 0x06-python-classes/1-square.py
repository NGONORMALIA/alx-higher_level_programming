#!/usr/bin/python3
"""module to define a square and some instantiation
 and private instance atribute"""


class Square:
    """class to define square with instance
    Args:
        size:the size of our square
    """
    def __init__(self, size):
        """initialisation of our class
        Args:
            self: the default argument of our function
            size: the size of our function
        """
        self.__size = size
