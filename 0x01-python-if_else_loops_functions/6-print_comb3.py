#!/usr/bin/python3
for i in range(0, 100):
    num1 = i / 10
    num2 = i % 10
    if i == 89:
        print('{:d}'.format(i))
    elif num1 < num2:
        print('{:02d}'.format(i), end=", ")
