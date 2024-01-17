#!/usr/bin/python3
def remove_char_at(str, n):
    d = ''
    for i in range(len(str)):
        if i != n:
            d = d + str[i]
    return d
