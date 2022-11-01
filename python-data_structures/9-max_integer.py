#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        if len(my_list) == 1:
            return my_list[0]
        else:
            op1 = my_list[0]
            op2 = max_integer(my_list[1:])

            if op1 > op2:
                return op1
            else:
                return op2
