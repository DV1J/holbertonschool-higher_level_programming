#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_newlist = []
    for i in range(len(my_list)):
        my_newlist.append(my_newlist[i])
    return(my_newlist)