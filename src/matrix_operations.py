import numpy as np
from typing import List, Union


def calc_determinant(matrix: List[List[Union[int, float]]]) -> float:
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (lList[List[Union[int, float]]]): A square matrix represented as a list of lists.

    Returns:
        float: The determinant of the matrix.
    """
    np_matrix = np.array(matrix)
    return round(float(np.linalg.det(np_matrix)), 2)


def calc_transpose(
    matrix: List[List[Union[int, float]]],
) -> List[List[Union[int, float]]]:
    """
    Calculate the transpose of a matrix.

    Args:
        matrix (List[List[Union[int, float]]]): A matrix represented as a list of lists.

    Returns:
        List[List[Union[int, float]]]: The transposed matrix.
    """
    np_matrix = np.array(matrix)
    transposed = np_matrix.T
    return transposed.tolist()


def calc_multiply(
    matrix_a: List[List[Union[int, float]]], matrix_b: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    Multiply two matrices.

    Args:
        matrix_a (List[List[Union[int, float]]]): The first matrix.
        matrix_b (List[List[Union[int, float]]]): The second matrix.

    Returns:
        List[List[Union[int, float]]]: The resulting matrix after multiplication.
    """
    np_matrix_a = np.array(matrix_a)
    np_matrix_b = np.array(matrix_b)
    result = np.matmul(np_matrix_a, np_matrix_b)
    return result.tolist()
