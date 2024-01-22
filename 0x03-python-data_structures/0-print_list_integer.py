#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print integer in list

    Args:
        my_list: the list to print from

    Returns:
        NULL
    """
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
