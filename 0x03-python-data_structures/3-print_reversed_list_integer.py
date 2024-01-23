#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if n == 0 or my_list is None:
        return None
    for i in range(n):
        print("{:d}".format(my_list[n-i-1]))
