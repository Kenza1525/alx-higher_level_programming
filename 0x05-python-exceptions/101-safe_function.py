#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as err:
        print("Exception: {}".format(err), file=stderr)
        return None
