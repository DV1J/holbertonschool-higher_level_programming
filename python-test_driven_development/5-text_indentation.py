#!/usr/bin/python3
"""A function that indents texts after (., ?, :)
"""


def text_indentation(text):
    """Checking is text is a string if not Raise TypeError
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    new_line= True
    for i in text:
        if new_line and i == ' ':
            continue
        new_line = False
        if i in ('.','?',':'):
            print(i)
            print()
            new_line = True
        else:
            print(i, end='')
