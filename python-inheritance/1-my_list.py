#!/usr/bin/python3
"""A class that inherits from list
"""
class MyList(list):
    def print_sorted(self):
        """printing sorted list
        """
        print(sorted(self))
