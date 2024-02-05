#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or x < 0:
        return (0)
    try:
        k = 0
        for i in my_list:
            if k == (x - 1):
                k += 1
                print(i)
            elif k < x:
                k += 1
                print("{}".format(i), end="")
    except IndexError:
        print("")
        return k
    return k
