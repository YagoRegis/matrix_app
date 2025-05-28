from . import schemas

def is_square(matrix):
    return all(len(row) == len(matrix) for row in matrix)

def select_matrix_input(payload: schemas.MatrixOperation):
    if payload.matrix_id_a:
        return payload.matrix_id_a
    elif payload.matrix_id_b:
        return payload.matrix_id_b
    elif payload.matrix_a:
        return payload.matrix_a
    elif payload.matrix_b:
        return payload.matrix_b
    else:
        return None