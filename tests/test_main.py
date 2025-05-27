import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src import database, models

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_matrices.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override the get_db function to return a mock session."""
    models.Base.metadata.create_all(bind=engine)  # Create tables for testing
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

client = TestClient(app)

def test_create_matrix():
    payload = {
        "name": "Test Matrix",
        "data": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    }
    
    response = client.post("/matrix/create", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["data"] == payload["data"]