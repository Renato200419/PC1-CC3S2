import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.crud import create_jugador, get_jugador_by_name
from app.models import Jugador  # Importa el modelo para usar en los mocks

# Configurar el cliente de pruebas para la aplicación FastAPI
client = TestClient(app)

# Pruebas con Mocks para evitar conexión a la base de datos
class TestCRUDWithMocks(unittest.TestCase):

    @patch('app.crud.Jugador')  # Mockear el modelo de Peewee 'Jugador'
    @patch('app.crud.create_jugador')
    def test_create_jugador(self, mock_create_jugador, mock_jugador_model):
        # Arrange: Crear un mock del objeto Jugador
        mock_jugador = mock_jugador_model.create.return_value
        mock_jugador.nombre = "NuevoJugador"
        mock_create_jugador.return_value = mock_jugador

        # Act: Llamar a la función a probar
        jugador = create_jugador("NuevoJugador")

        # Assert: Verificar que se llamó al mock y se obtuvo el valor esperado
        mock_jugador_model.create.assert_called_once_with(nombre="NuevoJugador")
        self.assertEqual(jugador.nombre, "NuevoJugador")

    @patch('app.crud.Jugador')  # Mockear el modelo de Peewee 'Jugador'
    @patch('app.crud.get_jugador_by_name')
    def test_get_jugador_by_name(self, mock_get_jugador_by_name, mock_jugador_model):
        # Arrange: Crear un mock del objeto Jugador
        mock_jugador = mock_jugador_model.get_or_none.return_value
        mock_jugador.nombre = "TestJugador"
        mock_get_jugador_by_name.return_value = mock_jugador

        # Act: Llamar a la función a probar
        jugador = get_jugador_by_name("TestJugador")

        # Assert: Verificar que se llamó al mock y se obtuvo el valor esperado
        mock_jugador_model.get_or_none.assert_called_once_with(Jugador.nombre == "TestJugador")
        self.assertEqual(jugador.nombre, "TestJugador")

# Pruebas para rutas utilizando Mocks
class TestRoutesWithMocks(unittest.TestCase):

    @patch('app.crud.Jugador')  # Mockear el modelo de Peewee 'Jugador'
    @patch('app.routes.get_jugador_by_name')
    @patch('app.routes.create_jugador')
    def test_create_jugador_route(self, mock_create_jugador, mock_get_jugador_by_name, mock_jugador_model):
        # Arrange: Crear un mock del objeto Jugador y configurar las respuestas de los mocks
        mock_response = {"mensaje": "Jugador registrado exitosamente"}
        mock_create_jugador.return_value = MagicMock(nombre="JugadorAPI")

        # Simular que el jugador ya está registrado
        mock_get_jugador_by_name.return_value = MagicMock(nombre="JugadorAPI")  # Jugador ya registrado

        # Act: Llamar a la ruta a probar
        response = client.post("/jugadores/", json={"nombre": "JugadorAPI"})

        # Debug: Imprimir la respuesta para ver el contenido al fallar
        print("Response JSON:", response.json())

        # Assert: Verificar que se obtuvo el valor esperado (400 en caso de duplicado)
        self.assertEqual(response.status_code, 400)
        self.assertIn("El jugador ya está registrado", response.json()["detail"])

    @patch('app.crud.Jugador')  # Mockear el modelo de Peewee 'Jugador'
    @patch('app.routes.get_jugador_by_name')
    def test_get_jugador_by_name_route(self, mock_get_jugador_by_name, mock_jugador_model):
        # Arrange: Crear un mock del objeto Jugador
        mock_jugador = MagicMock(nombre="JugadorAPI")
        mock_get_jugador_by_name.return_value = mock_jugador

        # Act: Llamar a la ruta a probar
        response = client.get(f"/jugadores/{mock_jugador.nombre}")

        # Assert: Verificar que se llamó al mock y se obtuvo el valor esperado
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["nombre"], "JugadorAPI")
        mock_get_jugador_by_name.assert_called_once_with("JugadorAPI")


if __name__ == "__main__":
    unittest.main()