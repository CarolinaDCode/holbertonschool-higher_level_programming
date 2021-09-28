#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
    except BaseException as err:
        func = None
        print('Exception: {}'.format(err), file=sys.stderr)
    finally:
        return func
