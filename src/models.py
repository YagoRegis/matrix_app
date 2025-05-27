from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Matriz(Base):
    __tablename__ = "matrizes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    dados = Column(Text)  # JSON com a matriz
    data_criacao = Column(DateTime, default=datetime.utcnow)
