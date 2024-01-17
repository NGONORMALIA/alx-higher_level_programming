#!/usr/bin/python3
def uppercase(str):
    svt = ''
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            svt = svt + chr(ord(str[i]) - 32)
        else:
            svt = svt + str[i]
    print("{}".format(svt))
