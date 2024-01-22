#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
     """Print list in reverse order

    Args:
        my_list: the list to reverse

    Returns:
        Null
    """
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
