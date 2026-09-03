#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_nlist = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
            my_nlist.append(my_list[i])
        else:
            my_nlist.append(my_list[i])
    return (my_nlist)
