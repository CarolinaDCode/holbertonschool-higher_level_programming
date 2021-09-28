#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for i in range(0, x):
        if isinstance(my_list[i], int):
            try:
                cont += 1
                print('{:d}'.format(my_list[i]), end = '')
            except TypeError as err:
                print(err)
    print()
    return cont
