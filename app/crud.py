# app/crud.py
from .models import Jugador, Partida, JugadoresPartidas

# Crear un nuevo jugador
def create_jugador(nombre: str) -> Jugador:
    return Jugador.create(nombre=nombre)

# Obtener un jugador por nombre
def get_jugador_by_name(nombre: str) -> Jugador:
    return Jugador.get_or_none(Jugador.nombre == nombre)

# Crear una nueva partida con jugadores
def create_partida(jugadores: list) -> Partida:
    # Crear la partida
    partida = Partida.create(puntajes='{}')
    # Relacionar los jugadores con la partida
    for jugador in jugadores:
        JugadoresPartidas.create(jugador=jugador, partida=partida)
    return partida

# Obtener una partida por su ID
def get_partida_by_id(partida_id: int) -> Partida:
    return Partida.get_or_none(Partida.id == partida_id)

# Actualizar los puntajes de una partida
def update_puntajes(partida: Partida, nuevos_puntajes: dict) -> None:
    partida.puntajes = str(nuevos_puntajes)
    partida.save()
