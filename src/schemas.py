from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Union
from datetime import datetime


class MatrixBase(BaseModel):
    name: str
    data: List[List[Union[int, float]]]


class MatrixCreate(MatrixBase):
    pass


class MatrixRead(MatrixBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class MatrixOperation(BaseModel):
    matrix_id_a: Optional[int] = None  # ID of the first matrix
    matrix_id_b: Optional[int] = None  # ID of the second matrix
    matrix_a: List[List[Union[int, float]]] = None  # first matrix data
    matrix_b: List[List[Union[int, float]]] = None  # second matrix data


class MatrixOperationResult(BaseModel):
    result: Union[List[List[Union[int, float]]], int, float] = None
