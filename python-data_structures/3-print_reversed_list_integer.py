#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for item in my_list[::-1]:
        if my_list is None:
            return ''
        else:
            print("{:d}".format(item))
