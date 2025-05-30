import pytest

from src import matrix_operations

def test_determinant():
    matrix = [[1, 2], [3, 4]]
    result = matrix_operations.calc_determinant(matrix)
    
    assert result == -2.0  # Determinant of [[1, 2], [3, 4]] is -2

def test_transpose():
    matrix = [[1, 2], [3, 4]]
    result = matrix_operations.calc_transpose(matrix)
    
    assert result == [[1, 3], [2, 4]]  # Transpose of [[1, 2], [3, 4]] is [[1, 3], [2, 4]]

def test_multiply():
    matrix_a = [[1, 0], [0, 1]]
    matrix_b = [[4, 1], [2, 2]]
    result = matrix_operations.calc_multiply(matrix_a=matrix_a, matrix_b=matrix_b)
    assert result == [[4, 1], [2, 2]]  # Multiplication of identity matrix with another matrix should yield the same matrix