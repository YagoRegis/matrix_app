# 📐 Matrix Operations API — FastAPI + SQLite

This project is a RESTful API built with [FastAPI](https://fastapi.tiangolo.com/) to create, store, and perform mathematical operations on matrices, such as determinant calculation, transpose, and multiplication. It's ideal as a portfolio project or to study REST APIs, Pydantic, and SQLAlchemy.

---

## 🚀 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [NumPy](https://numpy.org/) (for matrix operations)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/matrix_app.git
cd matrix_app

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the API

```bash
uvicorn src.main:app --reload # --log-level debug
```

Open your browser at: [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI interactive documentation.

---

## 🧪 Example Usage

### 🔹 Create a Matrix
`POST /matriz/criar`

```json
{
  "nome": "Matrix A",
  "dados": [[1, 2], [3, 4]]
}
```

### 🔸 Expected Response

```json
{
  "id": 1,
  "nome": "Matrix A",
  "dados": [[1, 2], [3, 4]],
  "data_criacao": "2025-05-24T14:00:00"
}
```

---

## 📚 Project Structure

```
.
├── src/
├  ├── __init__.py      # module loader  
├  ├── main.py          # API entry point
├  ├── models.py        # SQLAlchemy ORM model
├  ├── schemas.py       # Pydantic validation
├  ├── database.py      # SQLite connection setup
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## 🛠️ Future Features

- [ ] Determinant calculation
- [ ] Matrix transpose
- [ ] Matrix multiplication
- [x] List and retrieve matrix history
- [ ] Basic authentication (optional)

---

## 🧑‍💻 Author

Developed by [Yago Regis Santos Rodrigues](https://github.com/YagoRegis)

---

## 📝 License

This project is licensed under the MIT License.
