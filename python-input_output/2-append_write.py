#!/usr/bin/python3
"""A function that append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """using with to open file with 'a' to append text
    """
    with open(filename, 'a') as f:
        f.write(text)
        """using loop to count charactors in string
        """
        count = 0
        for i in range(len(text)):
            count += 1
        return count
    f.closed
