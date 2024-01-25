#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    new = set(my_list)
    j = sum(new)
    return j
