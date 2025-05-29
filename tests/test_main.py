from fastapi.testclient import TestClient

def test_create_matrix(client: TestClient):
    payload = {
        "name": "Test Matrix",
        "data": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    }
    
    response = client.post("/matrix/create", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["data"] == payload["data"]

def test_get_matrix(client: TestClient):
    # Create
    payload = {
        "name": "Test Matrix",
        "data": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    }
    create_response = client.post("/matrix/create", json=payload)
    created = create_response.json()

    # Get by ID
    get_response = client.get(f"/matrix/{created['id']}")
    assert get_response.status_code == 200
    retrieved = get_response.json()
    assert retrieved["name"] == created["name"]
    assert retrieved["data"] == created["data"]
    assert retrieved["id"] == created["id"]


def test_create_invalid_matrix(client: TestClient):
    payload = {
        "name": "Invalid Matrix",
        "data": [[1, 2], [3, 4, 5]]  # row x columns mismatch
    }
    
    response = client.post("/matrix/create", json=payload)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Line and Columns must be the same length"}
    
def test_list_matrices(client: TestClient):
    # Create a matrix
    payload = {
        "name": "List Test Matrix",
        "data": [[1, 2], [3, 4]]
    }
    create_response = client.post("/matrix/create", json=payload)
    created = create_response.json()

    # List all matrices
    list_response = client.get("/matrices")
    assert list_response.status_code == 200
    all_matrices = list_response.json()
    
    assert isinstance(all_matrices, list)
    assert any(m["id"] == created["id"] for m in all_matrices)

def test_get_nonexistent_matrix(client: TestClient):
    response = client.get("/matrix/9999")  # Assuming 9999 does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Matrix with id 9999 not found"}

def test_calculate_determinant_by_matrix(client: TestClient):
    payload = {
        "matrix_a": [[1, 2], [3, 4]]
    }
    
    response = client.post("/matrix/determinant", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == -2.0  # Determinant of [[1, 2], [3, 4]] is -2

def test_calculate_determinant_wrong_matrix(client: TestClient):
    payload = {
        "matrix_a": [[1, 2, 3], [3, 4]]
    }
    
    response = client.post("/matrix/determinant", json=payload)
    
    assert response.status_code == 400
    data = response.json()
    assert response.json() == {"detail": "Line and Columns must be the same length"}

def test_calculate_determinant_empty_matrix(client: TestClient):
    payload = {}
    
    response = client.post("/matrix/determinant", json=payload)
    
    assert response.status_code == 400
    data = response.json()
    assert response.json() == {"detail": "At least one matrix input is required"}

def test_calculate_determinant_by_matrix_id(client: TestClient):
    # Create
    payload = {
        "name": "Test Matrix",
        "data": [[1, 2], [3, 4]]
    }
    create_response = client.post("/matrix/create", json=payload)
    created = create_response.json()
    print(created)
    payload = {
        "matrix_id_a": created["id"]  # Use the created matrix ID
    }
    
    response = client.post("/matrix/determinant", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == -2.0  # Determinant of [[1, 2], [3, 4]] is -2
