#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary)
    for i in a_dictionary:
        new_dic[i] *= 2
    return new_dic
