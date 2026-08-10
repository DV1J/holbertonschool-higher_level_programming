#!/usr/bin/python3

for n in "abcdefghijklmnopqrstuvwxyz":
    if n == "e" or n == "q": 
        continue
    print("{}".format(n), end="")