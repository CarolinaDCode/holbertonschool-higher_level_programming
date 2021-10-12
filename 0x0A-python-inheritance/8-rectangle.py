#!/usr/bin/python3
"""
module defines a class Rectangle that inherits methods of class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class Rectangle inherit from BaseGeometry
    Instantiaition of with and height definif in
    construtor of Rectangle.
    integer_validator will validate width and height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self._height = height
