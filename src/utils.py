from . import schemas

def is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def find_matrix(payload: schemas.MatrixOperation):
    rtn_item = None
    if payload.matrix_id_a:
        rtn_item = payload.matrix_id_a
        payload.matrix_id_a = None
    elif payload.matrix_id_b:
        rtn_item = payload.matrix_id_b
        payload.matrix_id_b = None
    elif payload.matrix_a:
        rtn_item = payload.matrix_a
        payload.matrix_a = None
    elif payload.matrix_b:
        rtn_item = payload.matrix_b
        payload.matrix_b = None
    
    return rtn_item


def select_matrix_input(payload: schemas.MatrixOperation, n=1):
    return_lst = []
    for item in range(n):
        matrix = find_matrix(payload)
        return_lst.append(matrix)

    return return_lst[0] if n == 1 else return_lst
