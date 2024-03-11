#!/usr/bin/python3
"""Module to return the sum of two integer
"""


def add_integer(a, b=98):
    """add_integer to return the sum two integer
    Args:
        a: the first integer/float
        b: thhe second integer/float

    Raise:
        Typeerror: if a or b is not an integer or a float

    Returns:
        the sum of the integer
    """
    typ = [int, float]
    if (type(a) in typ and type(b) in typ):
        return (int(a) + int(b))
    else:
        if (type(b) not in typ):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")
