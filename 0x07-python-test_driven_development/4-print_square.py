#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """
    function that prints a square with the character #:
    size is the size length of the square,
    if size is not integer, throw raise a TypeError,
    if size is less than 0, throw raise a ValueError,
    if size is a float and is less than 0, throw raise a TypeError.
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
