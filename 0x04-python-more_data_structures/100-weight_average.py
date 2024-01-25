#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    a = 0
    c = 0
    for row in my_list:
        b = 1
        c += row[1]
        for i in row:
            b *= i
        a += b
    return (a / c)
