from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import numpy as np
import json
import traceback
from . import database, models, schemas, utils, operations

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

    # Salvar em JSON
    new_matrix = models.Matrix(name=payload.name, data=json.dumps(payload.data))
    db.add(new_matrix)
    db.commit()
    db.refresh(new_matrix)
    new_matrix.data = json.loads(
        new_matrix.data
    )  # convertting JSON string back to list
    return new_matrix


@app.get("/matrix/{matrix_id}", response_model=schemas.MatrixRead)
def get_matrix(matrix_id: int, db: Session = Depends(database.get_db)):
    matrix = db.query(models.Matrix).filter(models.Matrix.id == matrix_id).first()
    if not matrix:
        raise HTTPException(
            status_code=404, detail=f"Matrix with id {matrix_id} not found"
        )
    matrix.data = json.loads(matrix.data)  # convertting JSON string back to list
    return matrix


@app.get("/matrices", response_model=List[schemas.MatrixRead])
def list_matrices(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    matrices = db.query(models.Matrix).offset(skip).limit(limit).all()
    for matrix in matrices:
        matrix.data = json.loads(matrix.data)

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
        matrix = (
            db.query(models.Matrix)
            .filter(models.Matrix.id == matrix_input)
            .first()
        )
        if not matrix:
            raise HTTPException(status_code=404, detail="Matrix not found")
        matrix_data = json.loads(matrix.data) 
    elif isinstance(matrix_input, list):
        matrix_data = matrix_input

    if not utils.is_square(matrix=matrix_data):
        raise HTTPException(
            status_code=400, detail="Line and Columns must be the same length"
        )

    determinant = operations.calc_determinant(matrix_data)
    return schemas.MatrixOperationResult(result=determinant)
