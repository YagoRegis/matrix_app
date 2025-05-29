import pytest

from src import matrix_operations

def test_determinant():
    matrix = [[1, 2], [3, 4]]
    result = matrix_operations.calc_determinant(matrix)
    
    assert result == -2.0  # Determinant of [[1, 2], [3, 4]] is -2