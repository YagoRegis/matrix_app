from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import numpy as np
import json
import traceback
from . import database, models, schemas

app = FastAPI()

database.create_db_and_tables()

@app.post("/matrix/create", response_model=schemas.MatrixRead)
def create_matrix(payload: schemas.MatrixCreate, db: Session = Depends(database.get_db)):
    # Validar se é matriz retangular
    lines = len(payload.data)
    columns = len(payload.data[0])
    for linha in payload.data:
        if lines != columns:
            raise HTTPException(status_code=400, detail="Line and Columns must be the same length")

    # Salvar em JSON
    new_matrix = models.Matrix(name=payload.name, dados=json.dumps(payload.data))
    db.add(new_matrix)
    db.commit()
    db.refresh(new_matrix)
    new_matrix.data = json.loads(new_matrix.data)  # convertting JSON string back to list
    return new_matrix
    
    
@app.get("/matrix/{matrix_id}", response_model=schemas.MatrixRead)
def get_matrix(matrix_id: int, db: Session = Depends(database.get_db)):
    matrix = db.query(models.Matrix).filter(models.Matrix.id == matrix_id).first()
    if not matrix:
        raise HTTPException(status_code=404, detail=f"Matrix with id {matrix_id} not found")
    matrix.data = json.loads(matrix.data)  # convertting JSON string back to list
    return matrix

@app.get("/matrices", response_model=List[schemas.MatrixRead])
def list_matrices(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    matrices = db.query(models.Matrix).offset(skip).limit(limit).all()
    for matrix in matrices:
        matrix.data = json.loads(matrix.data)

    return matrices