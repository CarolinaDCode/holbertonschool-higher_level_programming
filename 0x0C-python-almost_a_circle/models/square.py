#!/usr/bin/python3
"""Define the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter, validations"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Public Method that assigns a key/value
        argument to attributes
        """
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Public Method that returns the dictionary
        representation of a Square
        """
        dic = {}
        dic['id'] = self.id
        dic['x'] = self.x
        dic['size'] = self.size
        dic['y'] = self.y
        return dic
