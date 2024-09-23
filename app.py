from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
from typing import List
import random
import uvicorn

app = FastAPI()

instrumentator = Instrumentator()

jugadores_registrados = []

partidas = []

class Jugador(BaseModel):
    nombre: str

class Partida(BaseModel):
    id: int
    jugadores: List[Jugador]
    puntajes: dict

# Métricas
partidas_counter= Counter("partidas_creadas_totales","Total de partidas_creadas")
tiradas_counter = Counter("tiradas_totales", "Total de tiradas realizadas")
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")


@app.post("/jugadores/")
def registrar_jugador(jugador: Jugador):
    if jugador.nombre in [j.nombre for j in jugadores_registrados]:
        raise HTTPException(status_code=400, detail="El jugador ya está registrado")
    jugadores_registrados.append(jugador)
    jugadores_counter.inc()
    return {"mensaje": f"Jugador {jugador.nombre} registrado con éxito"}

@app.post("/partidas/")
def crear_partida(jugadores: List[Jugador]):
    if len(jugadores) < 2:
        raise HTTPException(status_code=400, detail="Se requieren al menos 2 jugadores")
    nueva_partida = Partida(id=len(partidas) + 1, jugadores=jugadores, puntajes={jugador.nombre: 0 for jugador in jugadores})
    partidas.append(nueva_partida)
    partidas_counter.inc()
    return {"mensaje": f"Partida {nueva_partida.id} creada con éxito", "partida": nueva_partida}

@app.post("/partidas/{partida_id}/lanzar")
@latencia_histogram.time() # Medir latencia
def lanzar_dados(partida_id: int):
    tiradas_counter.inc() # Incrementar el contador de tiradas
    partida = next((p for p in partidas if p.id == partida_id), None)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    for jugador in partida.jugadores:
        puntos = random.randint(1, 6)
        partida.puntajes[jugador.nombre] += puntos
    return {"mensaje": f"Dados lanzados en la partida {partida_id}", "puntajes": partida.puntajes}

@app.get("/partidas/{partida_id}/estadisticas")
def obtener_estadisticas(partida_id: int):
    partida = next((p for p in partidas if p.id == partida_id), None)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return {"partida_id": partida.id, "puntajes": partida.puntajes}

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Juego de Dados"}

instrumentator.instrument(app).expose(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
