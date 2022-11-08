#!/usr/bin/python3
"""Create a square """


class Square:
    '''
    Create a square
        Has a private Instance att: size
    '''

    def __init__(self, size=0, position=(0, 0)):
        ''' init size '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        "returns the size att"
        return self.__size
    
    @property
    def position(self):
        ''' Returns the value of position'''
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, size):
        '''asign the size to the size att'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end="")
                for o in range(self.__size):
                    print("#", end="")
                print()
