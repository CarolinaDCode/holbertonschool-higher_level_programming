#!/usr/bin/python3
"""Class Square define square"""


class Square:
    """Method that defines the size of a square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
