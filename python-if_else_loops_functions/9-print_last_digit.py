#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -(-number % 10)
    lad = number % 10
    print(lad, end='')
    return (lad)
