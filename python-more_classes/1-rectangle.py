#!/usr/bin/python3
'''Create a new class of Rectangle'''


class Rectangle:
    '''A class that creates a Rectangle class'''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Gives back the value of the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the value of Width '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def height(self):
        '''Gives back the value of the Height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the value of heigh '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value
