#!/usr/bin/python3
"""Module to print name
"""


def say_my_name(first_name, last_name=""):
    """to print full name of someone

    Args:
        first_name: the first name to print
        last_name: the last name to print

    raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string


    Return: no return

    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
