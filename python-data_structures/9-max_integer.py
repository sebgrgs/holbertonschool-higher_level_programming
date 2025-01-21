#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    num_max = my_list[0]

    for num in my_list:
        if num > num_max:
            num_max = num
    return num_max
