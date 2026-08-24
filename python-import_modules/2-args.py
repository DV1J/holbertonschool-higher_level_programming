#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    num = len(argv[1:])
    if num == 0:
        print(num, 'arguments')
    elif num == 1:
        print(num, 'argument:')
    elif num >= 2:
        print(num, 'arguments:')
    for j in argv[1:]:
        print("{}: {}".format(i, j))
        i += 1
