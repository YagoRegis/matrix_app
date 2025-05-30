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

def calc_transpose(matrix: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
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