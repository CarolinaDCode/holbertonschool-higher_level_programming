"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by `div`.
    Matrix must be a list of lists.
    Each sub-list must contain only integers or floats.
    Empty sub-lists are not allowed.
    Divisor must be greater than 0 and must be an int or float.
    """

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if not all(isinstance(x, (int, float)) for x in i):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) is 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for l in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), l)))

    return new_matrix
