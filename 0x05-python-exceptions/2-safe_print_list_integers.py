#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None or x < 0:
        return (0)
    i = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            i += 1
        except (TypeError, ValueError):
            continue
    print("")
    return i
