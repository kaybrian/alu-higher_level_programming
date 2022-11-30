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

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def display(self):
        """Returns rectangle #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.width = kwargs["width"] if "width" in kwargs \
                else self.width
            self.height = kwargs["height"] if "height" in kwargs \
                else self.height
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
