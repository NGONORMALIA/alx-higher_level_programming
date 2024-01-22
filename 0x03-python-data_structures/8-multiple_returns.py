#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        f = None
    else:
        f = sentence[0]
    t = n, f
    return t
