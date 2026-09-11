#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    n_list = my_list[:]
    return (list(map(lambda x: x * number, n_list)))
