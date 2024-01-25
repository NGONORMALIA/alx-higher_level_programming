#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    new = {}
    for k, va in a_dictionary.items():
        new.update([(k, va * 2)])
    return new
