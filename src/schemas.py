from pydantic import BaseModel
from typing import List, Union
from datetime import datetime

class MatrizBase(BaseModel):
    nome: str
    dados: List[List[Union[int, float]]]

class MatrizCreate(MatrizBase):
    pass

class MatrizRead(MatrizBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True
