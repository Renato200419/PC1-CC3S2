from .models import Jugador, Partida, JugadoresPartidas
from typing import List

# Crear un nuevo jugador
def create_jugador(nombre: str) -> Jugador:
    return Jugador.create(nombre=nombre)

# Obtener un jugador por nombre
def get_jugador_by_name(nombre: str) -> Jugador:
    return Jugador.get_or_none(Jugador.nombre == nombre)

# Crear una nueva partida con jugadores
def create_partida(jugadores: list) -> Partida:
    # Crear un diccionario de puntajes iniciales con los jugadores y sus puntajes en 0
    puntajes_iniciales = {jugador.nombre: 0 for jugador in jugadores}
    
    # Crear la partida con puntajes iniciales
    partida = Partida.create(puntajes=str(puntajes_iniciales))
    
    # Relacionar los jugadores con la partida
    for jugador in jugadores:
        JugadoresPartidas.create(jugador=jugador, partida=partida)
    
    return partida


# Obtener una partida por su ID
def get_partida_by_id(partida_id: int) -> Partida:
    return Partida.get_or_none(Partida.id == partida_id)

# Actualizar los puntajes de una partida
def update_puntajes(partida: Partida, nuevos_puntajes: dict) -> None:
    # Asegurarse de que nuevos_puntajes esté en el formato correcto
    if isinstance(nuevos_puntajes, dict):
        partida.puntajes = str(nuevos_puntajes)
        partida.save()
    else:
        raise ValueError("nuevos_puntajes debe ser un diccionario válido.")


# Obtener todos los jugadores
def get_all_jugadores() -> List[Jugador]:
    return Jugador.select()
