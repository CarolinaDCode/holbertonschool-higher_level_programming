#!/usr/bin/python3
"""Define a new class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    size will be private and will validated by integer_validator
    Class Square will also have method area
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
