#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        d = number % 10
    elif number < 0:
        d = (-1*number) % 10
    else:
        d = 0
    print("{}".format(d), end='')
    return d
