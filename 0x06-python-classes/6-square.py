#!/usr/bin/python3
"""module to define a square and some instantiation
 and private instance atribute"""


class Square:
    """class to define square with instance
    Args:
        size:the size of our square
    """
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """the function to get the position
        Return: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """funtion to set the value to position
        Args:
            value: the value to set to position
        Raises:
            TypeError: if position is not a tuple of two integer
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """function to return the area of our square
        Args:
            self: the default argument of our function
        return: the area of our square
        """
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print("")
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
