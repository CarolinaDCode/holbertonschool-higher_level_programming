#!/usr/bin/python3
def weight_average(my_list=[]):
    promedio = 0.0
    if not my_list:
        return 0

    numerador = list(t[0] * t[1] for t in my_list)
    denominador = list(t[1] for t in my_list)
    promedio = sum(numerador) / sum(denominador)
    return promedio
