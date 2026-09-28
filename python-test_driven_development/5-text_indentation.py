#!/usr/bin/python3
"""A function that indents texts after (., ?, :)
"""


def text_indentation(text):
    """Checking is text is a string if not Raise TypeError
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in text:
        if i != '.' and i != '?' and i != ':':
            text = text.rstrip()
            print(i, end='')
        else:
            text = text.rstrip()
            print(i)
            print()
