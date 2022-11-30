#!/usr/bin/python3
"""Rectangle class that inherts from Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherts from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width_value):
        """Width of the rectangle"""
        if width_value < 0:
            return ValueError("Width should be > 0")

        if type(width_value) != int:
            return TypeError("Width should be an integer")

        self.__width = width_value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height_value):
        """Height of the rectangle"""
        if height_value < 0:
            return ValueError("Height should be > 0")

        if type(height_value) != int:
            return TypeError("Height should be an integer")

    @property
    def x(self):
        """X coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x_value):
        """X coordinate of the rectangle"""
        if x_value < 0:
            return ValueError("X should be > 0")

        if type(x_value) != int:
            return TypeError("X should be an integer")

        self.__x = x_value

    @property
    def y(self):
        """Y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y_value):
        """Y coordinate of the rectangle"""
        if y_value < 0:
            return ValueError("Y should be > 0")

        if type(y_value) != int:
            return TypeError("Y should be an integer")

        self.__y = y_value
