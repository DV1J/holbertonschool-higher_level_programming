#!/usr/bin/python3
"""A class that inherits from list
"""


class MyList(list):
    """Public instance print_sorted"""
    def print_sorted(self):
        """printing sorted list
        """
        print(sorted(self))
