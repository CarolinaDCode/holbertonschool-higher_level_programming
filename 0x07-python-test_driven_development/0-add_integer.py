#!/usr/bin/python3
"""Define a function that add two integers"""


def add_integer(a, b=98):
    """
    Return the sum of the two integers or floats,
    if they are floats convert them to integers.
    If they are not, it throws a TypeError with a message.
    """

    if a is None (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')

    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
