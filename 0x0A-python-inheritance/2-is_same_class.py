#!/usr/bin/python3
"""
module defines a function
"""


def is_same_class(obj, a_class):
    """
    returns True if object is an instance of class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
