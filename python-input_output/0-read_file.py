#!/usr/bin/python3
"""A Function that reads a text file
"""
def read_file(filename=""):
    """opening file using with"""
    with open(filename) as f:
        read_data = f.read()
    f.closed
