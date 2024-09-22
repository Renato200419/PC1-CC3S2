import httpx

def test_root():
    response = httpx.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Juego de Dados"}

def test_crear_partida():
    jugadores = [{"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}]
    response = httpx.post("http://localhost:8000/partidas/", json=jugadores)
    assert response.status_code == 200
    assert "Partida" in response.json()["mensaje"]

def test_lanzar_dados():
    API_BASE_URL = "http://localhost:8000"
    response = httpx.post(f"{API_BASE_URL}/partidas/", json=[
        {"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}
    ])
    partida_id = response.json()['partida']['id']
    response = httpx.post(f"{API_BASE_URL}/partidas/{partida_id}/lanzar")
    assert response.status_code == 200
    assert "Dados lanzados" in response.json().get('mensaje')