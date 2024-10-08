# app/database.py

from .config import db  # Importar la configuración de la base de datos desde config.py

# Inicialización de la base de datos y creación de tablas
def initialize_db():
    from .models import Jugador, Partida, JugadoresPartidas  # Importar dentro de la función para evitar circularidad
    db.connect()
    db.create_tables([Jugador, Partida, JugadoresPartidas])
