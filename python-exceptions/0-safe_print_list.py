#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    final_list = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            final_list += 1
        except IndexError:
            continue
    print()
    return (final_list)
