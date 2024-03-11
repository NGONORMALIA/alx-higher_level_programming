#!/usr/bin/python3
"""Module to print square with # character with size length
"""


def print_square(size):
    """to print square with # character

    Agrs:
        size: the length of our square

    Raises:
        TypeError:size is not an integer or a float < 0
        ValueError:size is an integer less than 0
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
            if (j == (size - 1)):
                print("")
