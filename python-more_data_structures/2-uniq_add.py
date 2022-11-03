#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    uniq_add = set(my_list)
    return sum(uniq_add)
