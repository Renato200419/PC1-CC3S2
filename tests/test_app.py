import os
from fastapi.testclient import TestClient
from app.main import app

# Forzar la configuración de la URL de la base de datos a localhost
os.environ["DATABASE_URL"] = "postgresql://admin:secret@localhost:5432/dadosdb"

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Juego de Dados"}

def test_crear_partida():
    jugadores = [{"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}]
    response = client.post("/partidas/", json=jugadores)
    assert response.status_code == 200
    assert "Partida" in response.json()["mensaje"]

def test_lanzar_dados():
    jugadores = [{"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}]
    response = client.post("/partidas/", json=jugadores)
    partida_id = response.json()['partida']['id']

    response = client.post(f"/partidas/{partida_id}/lanzar")
    assert response.status_code == 200
    assert "Dados lanzados" in response.json().get('mensaje')
