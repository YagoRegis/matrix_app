import json
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from . import models, schemas
from .exceptions import NotFoundError

class RepositoryABC(ABC):
    """
    Abstract base class for repositories.
    """

    @abstractmethod
    def get(self, id: str) -> dict:
        """
        Retrieve an item by its ID.
        """
        pass

    @abstractmethod
    def save(self, item: dict) -> None:
        """
        Save an item to the repository.
        """
        pass

    @abstractmethod
    def list(self, skip: int, limit: int) -> None:
        """
        List items.
        """
        pass

class SQLAlchemyMatrixRepository(RepositoryABC):
    """
    SQLAlchemy implementation of the Matrix repository.
    """

    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int):
        matrix = self.session.query(models.Matrix).filter(models.Matrix.id == id).first()
        if matrix:
            matrix.data = json.loads(matrix.data)
            return matrix
        raise NotFoundError(f"Matrix with id {id} not found")

    def save(self, item: schemas.MatrixCreate):
        new_matrix = models.Matrix(name=item.name, data=json.dumps(item.data))
        self.session.add(new_matrix)
        self.session.commit()
        self.session.refresh(new_matrix)
        new_matrix.data = json.loads(new_matrix.data)
        return new_matrix

    def list(self, skip: int, limit: int) -> list:
        matrices = self.session.query(models.Matrix).offset(skip).limit(limit).all()
        for matrix in matrices:
            matrix.data = json.loads(matrix.data)
        return matrices