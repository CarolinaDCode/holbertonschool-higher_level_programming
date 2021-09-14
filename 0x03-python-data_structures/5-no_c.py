#!/usr/bin/python3
def no_c(my_string):
    string_sin_c = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            string_sin_c += my_string[i]
    return string_sin_c
