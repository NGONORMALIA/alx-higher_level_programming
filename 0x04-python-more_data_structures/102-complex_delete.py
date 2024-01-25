#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    new = {k: v for k, v in a_dictionary.items() if v == value}
    for ke in new.keys():
        del a_dictionary[ke]
    return a_dictionary
