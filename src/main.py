from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from . import database, matrix_operations, schemas, utils, repository
from .exceptions import NotFoundError

app = FastAPI()

database.create_db_and_tables()


@app.post("/matrix/create", response_model=schemas.MatrixRead)
def create_matrix(
    payload: schemas.MatrixCreate, db: Session = Depends(database.get_db)
):
    if not utils.is_square(matrix=payload.data):
        raise HTTPException(
            status_code=400, detail="Line and Columns must be the same length"
        )

    new_matrix = repository.SQLAlchemyMatrixRepository(session=db).save(item=payload)
    return new_matrix


@app.get("/matrix/{matrix_id}", response_model=schemas.MatrixRead)
def get_matrix(matrix_id: int, db: Session = Depends(database.get_db)):
    try:
        matrix = repository.SQLAlchemyMatrixRepository(session=db).get(id=matrix_id)
    except NotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Matrix with id {matrix_id} not found"
        )
    return matrix


@app.get("/matrices", response_model=List[schemas.MatrixRead])
def list_matrices(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    matrices = repository.SQLAlchemyMatrixRepository(session=db).list(
        skip=skip, limit=limit
    )

    return matrices


@app.post("/matrix/determinant", response_model=schemas.MatrixOperationResult)
def calculate_determinant(
    payload: schemas.MatrixOperation, db: Session = Depends(database.get_db)
):
    matrix_input = utils.select_matrix_input(payload=payload)
    if not matrix_input:
        raise HTTPException(
            status_code=400, detail="At least one matrix input is required"
        )
    elif isinstance(matrix_input, int):
        try:
            matrix_data = repository.SQLAlchemyMatrixRepository(session=db).get(
                id=matrix_input
            ).data
        except NotFoundError:
            raise HTTPException(
                status_code=404, detail=f"Matrix with id {matrix_input} not found"
            )
    elif isinstance(matrix_input, list):
        matrix_data = matrix_input

    if not utils.is_square(matrix=matrix_data):
        raise HTTPException(
            status_code=400, detail="Line and Columns must be the same length"
        )

    determinant = matrix_operations.calc_determinant(matrix_data)
    return schemas.MatrixOperationResult(result=determinant)

@app.post("/matrix/transpose", response_model=schemas.MatrixOperationResult)
def calculate_transpose(
    payload: schemas.MatrixOperation, db: Session = Depends(database.get_db)
):
    matrix_input = utils.select_matrix_input(payload=payload)
    if not matrix_input:
        raise HTTPException(
            status_code=400, detail="At least one matrix input is required"
        )
    elif isinstance(matrix_input, int):
        try:
            matrix_data = repository.SQLAlchemyMatrixRepository(session=db).get(
                id=matrix_input
            ).data
        except NotFoundError:
            raise HTTPException(
                status_code=404, detail=f"Matrix with id {matrix_input} not found"
            )
    elif isinstance(matrix_input, list):
        matrix_data = matrix_input

    transpose = matrix_operations.calc_transpose(matrix_data)
    return schemas.MatrixOperationResult(result=transpose)