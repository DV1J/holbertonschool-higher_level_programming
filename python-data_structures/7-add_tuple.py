#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    for i in range(len(tb)):
        for j in range(len(tb)):
            if ta > tb:
                tb[i] = 0
                tb[j] = 0
            add = (ta[i] + tb[i])
            add_2 = (ta[1] + tb[j])
        return(add, add_2)
