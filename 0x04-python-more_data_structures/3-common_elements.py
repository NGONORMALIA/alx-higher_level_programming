#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return (None)
    set = [x for x in set_1 if x in set_2]
    return set
