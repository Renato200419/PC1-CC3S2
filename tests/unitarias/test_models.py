# tests/test_models.py

import pytest
from peewee import SqliteDatabase, IntegrityError
from unittest.mock import patch
from app.models import Jugador, Partida, JugadoresPartidas

# Base de datos en memoria para pruebas
test_db = SqliteDatabase(":memory:")

@pytest.fixture(scope='function', autouse=True)
def mock_database():
    """Configurar la base de datos en memoria para las pruebas."""
    # Importar modelos y asignar base de datos
    with patch("app.models.db", test_db):
        from app.models import Jugador, Partida, JugadoresPartidas  # Reimportar con el mock
        test_db.bind([Jugador, Partida, JugadoresPartidas], bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables([Jugador, Partida, JugadoresPartidas])
        yield
        test_db.drop_tables([Jugador, Partida, JugadoresPartidas])
        test_db.close()

# Prueba para la creación de un jugador
def test_creacion_jugador():
    jugador = Jugador.create(nombre="JugadorTest")
    assert jugador.nombre == "JugadorTest"

# Prueba para asegurar que el nombre del jugador es único
def test_nombre_jugador_unico():
    jugador1 = Jugador.create(nombre="JugadorTest")
    with pytest.raises(IntegrityError):  # Se espera un error de integridad
        jugador2 = Jugador.create(nombre="JugadorTest")

# Prueba para la creación de una partida
def test_creacion_partida():
    partida = Partida.create(puntajes="{}")
    assert partida.puntajes == "{}"

# Prueba para asegurar la relación entre jugadores y partidas
def test_relacion_jugador_partida():
    jugador = Jugador.create(nombre="JugadorTest")
    partida = Partida.create(puntajes="{}")
    relacion = JugadoresPartidas.create(jugador=jugador, partida=partida)
    assert relacion.jugador == jugador
    assert relacion.partida == partida
