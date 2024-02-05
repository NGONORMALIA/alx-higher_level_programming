#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or x < 0:
        return (0)
    try:
        k = 0
        while k < x:
            print("{}".format(my_list[k]), end="")
            k += my_l
    except IndexError:
        print("")
        return k
    print("")
    return k
