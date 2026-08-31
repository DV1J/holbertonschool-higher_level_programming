#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    for i in range(len (tb)):
        if ta[i] < 2 or tb[i] < 2:
             ta[i] = 0
             tb[i] = 0
        add = (ta[i] + tb[i])
        print(add, end=' ')
