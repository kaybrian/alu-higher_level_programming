#!/usr/bin/python3
'''A python script that reads the contents of a file'''


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
