#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lad = -(-number % 10)
else: 
    lad = number % 10
if lad > 5:
    print(f"Last digit of {number} is {lad} and is greater than 5")
elif lad != 0:
    print(f"Last digit of {number} is {lad} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lad} and is 0")
