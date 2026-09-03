#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_nlist = my_list[:]
    for i in range(len(my_list)):
        if my_nlist[i] == search:
            my_nlist[i] = replace
    return (my_nlist)
