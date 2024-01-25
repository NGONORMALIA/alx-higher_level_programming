#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is None:
        return None
    new = sorted(a_dictionary)
    for i, v in new.items():
        print("{}: {}".format(i, v))
