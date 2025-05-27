from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC

Base = declarative_base()


class Matrix(Base):
    __tablename__ = "matrices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    data = Column(Text)  # JSON com a matriz
    created_at = Column(DateTime, default=datetime.now(UTC))
