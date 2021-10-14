#!/usr/bin/python3
"""Contains the pascal_triangle function"""


def pascal_triangle(n):
    """Returns a pascal triangle of n size"""
    arr = []
    if n <= 0:
        return arr
    for i in range(n):
        err = []
        err.append(1)
        if i == 0:
            arr.append(err)
            continue
        for j in range(1, i):
            try:
                err.append(arr[i-1][j-1] + arr[i-1][j])
            except:
                continue
        err.append(1)
        arr.append(err)

    return arr
