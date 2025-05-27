from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import numpy as np
import json
import traceback
from . import database, models, schemas

app = FastAPI()

database.create_db_and_tables()

@app.post("/matriz/criar", response_model=schemas.MatrizRead)
def criar_matriz(payload: schemas.MatrizCreate, db: Session = Depends(database.get_db)):
    # Validar se é matriz retangular
    linhas = len(payload.dados)
    colunas = len(payload.dados[0])
    for linha in payload.dados:
        if linhas != colunas:
            raise HTTPException(status_code=400, detail="Todas as linhas devem ter o mesmo número de colunas")

    # Salvar em JSON
    nova_matriz = models.Matriz(nome=payload.nome, dados=json.dumps(payload.dados))
    db.add(nova_matriz)
    db.commit()
    db.refresh(nova_matriz)
    nova_matriz.dados = json.loads(nova_matriz.dados)  # Converter de volta para lista
    return nova_matriz
    
    
@app.get("/matriz/{matriz_id}", response_model=schemas.MatrizRead)
def obter_matriz(matriz_id: int, db: Session = Depends(database.get_db)):
    matriz = db.query(models.Matriz).filter(models.Matriz.id == matriz_id).first()
    if not matriz:
        raise HTTPException(status_code=404, detail="Matriz não encontrada")
    matriz.dados = json.loads(matriz.dados)  # Converter de volta para lista
    return matriz

@app.get("/matriz", response_model=List[schemas.MatrizRead])
def listar_matrizes(db: Session = Depends(database.get_db)):
    matrizes = db.query(models.Matriz).all()
    for matriz in matrizes:
        matriz.dados = json.loads(matriz.dados)

    return matrizes