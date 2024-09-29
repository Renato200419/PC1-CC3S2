# app/database.py
from peewee import PostgresqlDatabase
from app.models import Jugador, Partida, JugadoresPartidas

# Configuración de la conexión a la base de datos PostgreSQL
db = PostgresqlDatabase(
    'dadosdb',  # Nombre de la base de datos
    user='admin',  # Usuario de la base de datos
    password='secret',  # Contraseña de la base de datos
    host='localhost',  # Cambiar 'db' a 'localhost'
    port=5432  # Puerto de la base de datos
)

# Inicialización de la base de datos y creación de tablas
def initialize_db():
    if not db.is_closed():
        db.close()
    db.connect()
    db.create_tables([Jugador, Partida, JugadoresPartidas])
