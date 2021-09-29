#!/usr/bin/python3
""" Class Square define square"""


class Square:
    """Class define size square"""
    def __init__(self, size=0):
        self.size = size

    """method getter / decorator"""
    @property
    def size(self):
        return self.__size

    """method setter / decorator"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """define square area"""
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
