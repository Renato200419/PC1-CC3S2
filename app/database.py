# app/database.py

from .config import db  # Importar la configuración de la base de datos desde config.py

# Inicialización de la base de datos y creación de tablas
def initialize_db():
    db.connect()
    db.create_tables([Jugador, Partida, JugadoresPartidas])
