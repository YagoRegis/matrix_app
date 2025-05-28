def is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)