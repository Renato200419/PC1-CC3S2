from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from prometheus_client import Counter, Histogram
from .crud import create_jugador, get_jugador_by_name,get_all_jugadores, create_partida, get_partida_by_id, update_puntajes
import random

# Crear el enrutador de FastAPI
router = APIRouter()

# Métricas de Prometheus
jugadores_counter = Counter("jugadores_registrados_totales", "Total de jugadores registrados")
partidas_counter = Counter("partidas_creadas_totales", "Total de partidas creadas")
tiradas_counter = Counter("tiradas_totales", "Total de tiradas realizadas")
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")
puntajes_histogram = Histogram("puntajes_altos", "Distribución de puntuaciones altas", buckets=[10, 20, 30, 40, 50, 60])

# Esquemas de Pydantic para validación de datos
class Jugador(BaseModel):
    nombre: str

class Partida(BaseModel):
    id: int
    jugadores: List[Jugador]
    puntajes: dict

# Rutas de la API
@router.post("/jugadores/")
def registrar_jugador(jugador: Jugador):
    if get_jugador_by_name(jugador.nombre):
        raise HTTPException(status_code=400, detail="El jugador ya está registrado")
    create_jugador(jugador.nombre)
    jugadores_counter.inc()  # Incrementar el contador de jugadores
    return {"mensaje": f"Jugador {jugador.nombre} registrado con éxito"}
#LISTAR LOS JUGADORES:
@router.get("/jugadores/")
def listar_jugadores():
    jugadores = get_all_jugadores()
    if not jugadores:
        return {"mensaje": "No hay jugadores registrados"}
    return {"jugadores": [jugador.nombre for jugador in jugadores]}

@router.post("/partidas/")
def crear_partida_endpoint(jugadores: List[Jugador]):
    if len(jugadores) < 2:
        raise HTTPException(status_code=400, detail="Se requieren al menos 2 jugadores")
    # Crear jugadores si no existen y registrar la partida
    jugador_objs = [get_jugador_by_name(j.nombre) or create_jugador(j.nombre) for j in jugadores]
    nueva_partida = create_partida(jugador_objs)
    partidas_counter.inc()  # Incrementar el contador de partidas
    return {"mensaje": f"Partida {nueva_partida.id} creada con éxito", "partida": nueva_partida}

@router.post("/partidas/{partida_id}/lanzar")
@latencia_histogram.time()  # Medir la latencia del endpoint
def lanzar_dados(partida_id: int):
    tiradas_counter.inc()  # Incrementar el contador de tiradas
    partida = get_partida_by_id(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    puntajes = eval(partida.puntajes)  # Convertir el string a diccionario
    for jugador in partida.jugadores:
        puntos = random.randint(1, 6)
        puntajes[jugador.jugador.nombre] = puntajes.get(jugador.jugador.nombre, 0) + puntos
        if puntos > 4:
            puntajes_histogram.observe(puntos)  # Agregar métrica para puntuaciones altas
    update_puntajes(partida, puntajes)
    return {"mensaje": f"Dados lanzados en la partida {partida_id}", "puntajes": puntajes}

@router.get("/partidas/{partida_id}/estadisticas")
def obtener_estadisticas(partida_id: int):
    partida = get_partida_by_id(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    puntajes = eval(partida.puntajes)
    return {"partida_id": partida.id, "puntajes": puntajes}

@router.post("/partidas/{partida_id}/reiniciar")
def reiniciar_partida(partida_id: int):
    partida = get_partida_by_id(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    puntajes = {jugador.jugador.nombre: 0 for jugador in partida.jugadores}
    update_puntajes(partida, puntajes)
    return {"mensaje": f"Partida {partida_id} reiniciada con éxito", "puntajes": puntajes}