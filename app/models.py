# app/models.py
from peewee import Model, CharField, ForeignKeyField, IntegerField
from .database import db

# Clase base para todos los modelos
class BaseModel(Model):
    class Meta:
        database = db
# Definición del modelo Jugador
class Jugador(BaseModel):
    nombre = CharField(unique=True) # Campo nombre único para cada jugador

# Definición del modelo Partida
class Partida(BaseModel):
    id = IntegerField(primary_key=True) # Campo id como clave primaria
    puntajes = CharField() # Almacenar los puntajes como un string JSON

# Definición del modelo intermedio JugadoresPartidas
class JugadoresPartidas(BaseModel):
    jugador = ForeignKeyField(Jugador, backref='partidas') # Relación con Jugador
    partida = ForeignKeyField(Partida, backref='jugadores') # Relación con Partida