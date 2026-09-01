#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    if len(tb) < 2:
        if len(ta) == 0:
            ta = 0, 0
        else:
            ta = ta[0], 0
    if len(tb) < 2:
        if len(tb) == 0:
            tb = 0, 0
        else:
            tb = tb[0], 0
    add = (ta[0] + tb[0])
    add_2 = (ta[1] + tb[1])
    return (add, add_2)
