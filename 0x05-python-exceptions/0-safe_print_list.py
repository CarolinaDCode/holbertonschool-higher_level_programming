#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cont = 0
        for i in range(0, x):
            cont += 1
            print('{}'.format(my_list[i]), end='')
        print()
        return x
    except IndexError:
        print()
        return i
