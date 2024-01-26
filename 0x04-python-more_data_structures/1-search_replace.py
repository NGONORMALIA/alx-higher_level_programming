#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return([])
    new = []
    for k in my_list:
        if k == search:
            new.append(replace)
        else:
            new.append(k)
    return new
