#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10

str = "Last digit of"
if last > 5:
    print('{} {:d} is {:d} and is greater than 5'.format(str, number, last))
elif last == 0:
    print('{} {:d} is {:d} and is 0'.format(str, number, last))
elif last < 6 and last != 0:
    print('{} {:d} is {:d} and is less than 6 and not 0'
          .format(str, number, last))
