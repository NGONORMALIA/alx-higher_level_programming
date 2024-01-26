#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    new = {}
    for k in a_dictionary:
        new[k] = a_dictionary[k] * 2
    return new
