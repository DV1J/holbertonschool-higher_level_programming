#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    if len(argv[1:]) == 0:
        print('0')
    for i in (argv[1:]):
        sum = sum + int(i)
    print(sum)
