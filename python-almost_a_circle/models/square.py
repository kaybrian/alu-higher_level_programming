#!/usr/bin/python3
"""Create a Square class for the work"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Create a Square class for the work"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Create a Square class for the work

        :param size: The size of the square
        :param x: The x coordinate of the square
        :param y: The y coordinate of the square
        :param id: The id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Return the size of the square

        :return: The size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        :param value: The size of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the string representation of the square

        :return: The string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
