# tests/test_routes.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_all_pokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json() == []

def test_read_single_pokemon():
    response = client.get("/pokemons/1")
    assert response.status_code == 404

# Puedes seguir agregando más pruebas para otras rutas y funcionalidades de tu aplicación CRUD
