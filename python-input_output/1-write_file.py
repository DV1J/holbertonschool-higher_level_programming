#!/usr/bin/python3
"""A function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """using with to open file and writing into it"""
    with open(filename, "w") as f:
        f.write(text)
        """ a loop to count the characters in text"""
        count = 0
        for i in range(len(text)):
            count += 1
        return count
    f.closed
