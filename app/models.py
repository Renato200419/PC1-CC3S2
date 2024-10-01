from peewee import Model, CharField, ForeignKeyField, AutoField, IntegerField
from .database import db

# Clase base para todos los modelos
class BaseModel(Model):
    class Meta:
        database = db

# Definición del modelo Jugador
class Jugador(BaseModel):
    nombre = CharField(unique=True)  # Campo nombre único para cada jugador
    victorias = IntegerField(default=0)  # Atributo que cuenta las victorias del jugador

    class Meta:
        table_name = 'jugador'  # Nombre de la tabla en la base de datos

# Definición del modelo Partida
class Partida(BaseModel):
    id = AutoField()  # AutoField asegura que id sea autoincremental y se genere automáticamente
    puntajes = CharField()  # Almacenar los puntajes como un string JSON

    class Meta:
        table_name = 'partida'  # Nombre de la tabla en la base de datos

# Definición del modelo intermedio JugadoresPartidas
class JugadoresPartidas(BaseModel):
    jugador = ForeignKeyField(Jugador, backref='partidas')  # Relación con Jugador
    partida = ForeignKeyField(Partida, backref='jugadores')  # Relación con Partida

    class Meta:
        table_name = 'jugadores_partidas'  # Nombre de la tabla en la base de datos
