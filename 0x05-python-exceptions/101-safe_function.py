#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return res
    except sys.exc_info()[0]:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return None
