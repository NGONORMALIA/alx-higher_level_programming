#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    d = number % 10
    if d > 5:
        print(f"Last digit of {number} is {d} and is greater than 5")
    elif d < 6 and d != 0:
        print(f"Last digit of {number} is {d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {d} and is 0")
elif number < 0:
    d = -1*((-1*number) % 10)
    if d == 0:
        print(f"Last digit of {number} is {d} and is 0")
    else:
        print(f"Last digit of {number} is {d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
