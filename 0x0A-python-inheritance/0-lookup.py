#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return the list attributes and methods of an objects.
    """
    return (dir(obj))