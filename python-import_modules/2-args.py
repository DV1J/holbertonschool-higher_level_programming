^#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if num == 1:
        print('0', 'arguments')
    elif num == 2:
        print('1', 'argument')
    elif num > 2:
        print(num, 'arguments')
    for j in argv[1:]:
        print("{}: {}".format(num, j)) 
