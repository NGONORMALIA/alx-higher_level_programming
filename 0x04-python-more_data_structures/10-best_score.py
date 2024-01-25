#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mx = -111000000825
    for k, v in a_dictionary.items():
        if v > mx:
            mx = v
            mx_key = k
    return mx_key
