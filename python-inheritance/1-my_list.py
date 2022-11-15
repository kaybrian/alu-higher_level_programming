#!/usr/bin/python3
'''This file creates a class that inherits from List builtin functions '''


class MyList(list):
    '''This Class inherits the built in function list'''

    def print_sorted(self):
        sorted_list = sorted(self[:])
        print("{}".format(sorted_list))
