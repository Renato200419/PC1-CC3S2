from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()
jugadores_registrados = []

class Jugador(BaseModel):
    nombre: str

@app.post("/jugadores/")
def registrar_jugador(jugador: Jugador):
    if jugador.nombre in [j.nombre for j in jugadores_registrados]:
        raise HTTPException(status_code=400, detail="El jugador ya está registrado")
    jugadores_registrados.append(jugador)
    return {"mensaje": f"Jugador {jugador.nombre} registrado con éxito"}

class Partida(BaseModel):
    id: int
    jugadores: List[Jugador]
    puntajes: dict

partidas = []

@app.post("/partidas/")
def crear_partida(jugadores: List[Jugador]):
    if len(jugadores) < 2:
        raise HTTPException(status_code=400, detail="Se requieren al menos 2 jugadores")
    nueva_partida = Partida(id=len(partidas) + 1, jugadores=jugadores, puntajes={jugador.nombre: 0 for jugador in jugadores})
    partidas.append(nueva_partida)
    return {"mensaje": f"Partida {nueva_partida.id} creada con éxito", "partida": nueva_partida}

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Juego de Dados"}