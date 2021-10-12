#!/usr/bin/python3
"""module defines a class BaseGeometry"""


class BaseGeometry:
    """area: public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator: define integer validator as method"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
