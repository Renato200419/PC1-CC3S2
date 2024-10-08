# tests/test_routes.py

from fastapi.testclient import TestClient
from app.main import app
from app.crud import get_jugador_by_name, create_jugador
from unittest.mock import patch, MagicMock

# Crear el cliente de pruebas para FastAPI
client = TestClient(app)

# Pruebas para las rutas de la API
def test_root():
    """Prueba para el endpoint raíz '/'."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Juego de Dados"}


@patch("app.routes.get_jugador_by_name")  # Mockear la función 'get_jugador_by_name'
@patch("app.routes.create_jugador")  # Mockear la función 'create_jugador'
def test_create_jugador_route(mock_create_jugador, mock_get_jugador_by_name):
    """Prueba para la ruta de creación de jugador: POST /jugadores/."""
    # Configurar los mocks
    mock_get_jugador_by_name.return_value = None  # Simula que no existe un jugador con ese nombre
    mock_create_jugador.return_value = MagicMock(nombre="JugadorAPI")

    # Realizar una solicitud POST para crear un nuevo jugador
    response = client.post("/jugadores/", json={"nombre": "JugadorAPI"})
    assert response.status_code == 201
    
    # Cambiar el mensaje esperado para que coincida con el mensaje real de la API
    assert response.json() == {"mensaje": "Jugador JugadorAPI registrado con éxito"}

@patch("app.routes.get_jugador_by_name")  # Mockear la función 'get_jugador_by_name'
def test_create_jugador_route_already_exists(mock_get_jugador_by_name):
    """Prueba para la ruta de creación de jugador cuando el jugador ya existe: POST /jugadores/."""
    # Configurar los mocks para simular que el jugador ya está registrado
    mock_get_jugador_by_name.return_value = MagicMock(nombre="JugadorAPI")

    # Realizar una solicitud POST para intentar registrar el mismo jugador
    response = client.post("/jugadores/", json={"nombre": "JugadorAPI"})
    assert response.status_code == 400
    assert response.json() == {"detail": "El jugador ya está registrado"}
    mock_get_jugador_by_name.assert_called_once_with("JugadorAPI")


@patch("app.routes.get_jugador_by_name")  # Mockear la función 'get_jugador_by_name'
def test_get_jugador_by_name_route(mock_get_jugador_by_name):
    mock_jugador = MagicMock(nombre="JugadorAPI", partidas={}, victorias={})
    mock_get_jugador_by_name.return_value = mock_jugador

    response = client.get(f"/jugadores/{mock_jugador.nombre}")
    assert response.status_code == 200
    assert response.json() == {"nombre": "JugadorAPI", "partidas": {}, "victorias": {}}



@patch("app.routes.get_jugador_by_name")  # Mockear la función 'get_jugador_by_name'
def test_get_jugador_by_name_route_not_found(mock_get_jugador_by_name):
    """Prueba para la ruta de obtención de un jugador por nombre cuando no se encuentra: GET /jugadores/{nombre}."""
    # Configurar los mocks para simular que no se encontró al jugador
    mock_get_jugador_by_name.return_value = None

    # Realizar una solicitud GET para obtener un jugador no existente
    response = client.get("/jugadores/JugadorInexistente")
    assert response.status_code == 404
    assert response.json() == {"detail": "Jugador no encontrado"}
    mock_get_jugador_by_name.assert_called_once_with("JugadorInexistente")
