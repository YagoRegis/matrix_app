from pydantic import BaseModel, ConfigDict
from typing import List, Union
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
