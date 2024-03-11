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
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """function to get the size of our square
        Args:
        self: the default argument of our function

        return: the got value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """function to set the new value to our square
        Args:
            self: the default argument of our function
            value:the new to set as a new size of our square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function to return the area of our square
        Args:
            self: the default argument of our function
        return: the area of our square
        """
        return self.__size ** 2
