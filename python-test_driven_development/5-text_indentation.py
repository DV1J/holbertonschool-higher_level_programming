#!/usr/bin/python3
"""A function that indents texts after (., ?, :)
"""


def text_indentation(text):
    """Checking is text is a string if not Raise TypeError
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in text:
        if i != '.' and i != '?' and i != ':':
            print(i, end='')
        else:
            print(i)
            
