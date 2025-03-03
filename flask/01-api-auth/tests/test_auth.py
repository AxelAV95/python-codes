import pytest
from src import create_app
from src.database import db
from src.models.user import User
import json

@pytest.fixture
def app():
    """Crea una instancia de la app para pruebas"""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://root:tu_contraseña@localhost/auth_db_test",
    })
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """Crea un cliente de prueba"""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Inicializa la base de datos con un usuario de prueba"""
    with app.app_context():
        user = User(email="test@example.com", password="password123")
        db.session.add(user)
        db.session.commit()

def test_register_success(client):
    """Prueba el registro exitoso de un usuario"""
    response = client.post(
        "/auth/register",
        data=json.dumps({"email": "newuser@example.com", "password": "password123"}),
        content_type="application/json"
    )
    assert response.status_code == 201
    assert b"User created successfully" in response.data

def test_register_existing_user(client, init_database):
    """Prueba registrar un usuario que ya existe"""
    response = client.post(
        "/auth/register",
        data=json.dumps({"email": "test@example.com", "password": "password123"}),
        content_type="application/json"
    )
    assert response.status_code == 400
    assert b"User already exists" in response.data

def test_login_success(client, init_database):
    """Prueba login exitoso"""
    response = client.post(
        "/auth/login",
        data=json.dumps({"email": "test@example.com", "password": "password123"}),
        content_type="application/json"
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "token" in data

def test_login_invalid_credentials(client, init_database):
    """Prueba login con credenciales inválidas"""
    response = client.post(
        "/auth/login",
        data=json.dumps({"email": "test@example.com", "password": "wrongpassword"}),
        content_type="application/json"
    )
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

def test_public_endpoint(client):
    """Prueba endpoint público"""
    response = client.get("/api/public")
    assert response.status_code == 200
    assert b"This is a public endpoint" in response.data

def test_protected_endpoint_no_token(client):
    """Prueba endpoint protegido sin token"""
    response = client.get("/api/protected")
    assert response.status_code == 401
    assert b"Token is missing" in response.data

def test_protected_endpoint_valid_token(client, init_database):
    """Prueba endpoint protegido con token válido"""
    # Primero obtenemos un token
    login_response = client.post(
        "/auth/login",
        data=json.dumps({"email": "test@example.com", "password": "password123"}),
        content_type="application/json"
    )
    token = json.loads(login_response.data)["token"]
    
    # Luego probamos el endpoint protegido
    response = client.get(
        "/api/protected",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert b"This is a protected endpoint" in response.data
