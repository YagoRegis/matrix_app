import pytest

from src import operations

def test_determinant():
    matrix = [[1, 2], [3, 4]]
    result = operations.calc_determinant(matrix)
    
    assert result == -2.0  # Determinant of [[1, 2], [3, 4]] is -2