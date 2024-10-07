from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from prometheus_client import Counter, Histogram
from .crud import create_jugador, get_jugador_by_name, get_all_jugadores, create_partida, get_partida_by_id, update_puntajes
import random

# Crear el enrutador de FastAPI
router = APIRouter()

# Métricas de Prometheus
jugadores_counter = Counter("jugadores_registrados_totales", "Total de jugadores registrados")
partidas_counter = Counter("partidas_creadas_totales", "Total de partidas creadas")
tiradas_counter = Counter("tiradas_totales", "Total de tiradas realizadas")
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")

# Métrica para contar cuántas veces se obtienen puntuaciones altas (puntuaciones de 6 en los dados)
puntuaciones_altas_counter = Counter("puntuaciones_altas", "Total de veces que se han obtenido puntuaciones altas (número 6)")

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

# Listar jugadores registrados
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

    # Verificar que todos los jugadores estén registrados previamente
    jugador_objs = []
    for j in jugadores:
        jugador = get_jugador_by_name(j.nombre)
        if not jugador:
            raise HTTPException(status_code=400, detail=f"El jugador '{j.nombre}' no está registrado.")
        jugador_objs.append(jugador)

    # Inicializar puntajes con 0 para cada jugador
    puntajes_iniciales = {jugador.nombre: 0 for jugador in jugador_objs}

    # Crear la partida con puntajes iniciales
    nueva_partida = create_partida(jugador_objs)
    nueva_partida.puntajes = str(puntajes_iniciales)
    nueva_partida.save()  # Guardar la partida con los puntajes iniciales

    partidas_counter.inc()  # Incrementar el contador de partidas
    return {"mensaje": f"Partida {nueva_partida.id} creada con éxito", "partida": nueva_partida}

@router.post("/partidas/{partida_id}/lanzar")
@latencia_histogram.time()
def lanzar_dados(partida_id: int):
    tiradas_counter.inc()
    partida = get_partida_by_id(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")

    # Convertir el string a diccionario solo si no está vacío
    puntajes = eval(partida.puntajes) if partida.puntajes else {}

    # Lógica para lanzar dados y acumular puntos
    for jugador_partida in partida.jugadores:
        jugador = jugador_partida.jugador  # Acceder al objeto Jugador a través de jugador_partida
        puntos = random.randint(1, 6)
        puntajes[jugador.nombre] = puntajes.get(jugador.nombre, 0) + puntos

        # Si el valor de puntos es 6, incrementamos el contador
        if puntos == 6:
            puntuaciones_altas_counter.inc()  # Incrementar el contador en 1 cada vez que se obtenga 6

    # Verificar si algún jugador alcanzó el puntaje máximo (por ejemplo, 50 puntos)
    ganador = None
    for jugador, puntaje in puntajes.items():
        if puntaje >= 50:  # Si el jugador alcanza 50 puntos o más
            ganador = jugador
            break

    # Si hay un ganador, finalizar la partida y actualizar el contador de victorias del jugador
    if ganador:
        jugador_ganador = get_jugador_by_name(ganador)
        jugador_ganador.victorias += 1
        jugador_ganador.partidas += 1  # Incrementar el número de partidas jugadas por el jugador ganador
        jugador_ganador.save()  # Guardar los cambios en la base de datos

        # Incrementar el contador de partidas jugadas para cada jugador
        for jugador in partida.jugadores:
            jugador.jugador.partidas += 1  # Incrementar el número de partidas jugadas para cada jugador
            jugador.jugador.save()

        return {
            "mensaje": f"¡La partida ha terminado! El ganador es {ganador} con {puntajes[ganador]} puntos.",
            "puntajes": puntajes
        }

    # Actualizar los puntajes de la partida si aún no hay ganador
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

# Mostrar ranking de jugadores
@router.get("/jugadores/ranking/")
def mostrar_ranking():
    # Obtener todos los jugadores y ordenarlos por victorias descendentes
    jugadores = get_all_jugadores()
    
    # Depuración: Asegúrate de que los jugadores obtenidos son instancias de Jugador
    print(f"Jugadores obtenidos: {jugadores}")
    
    # Ordenar por victorias descendentes
    jugadores_ordenados = sorted(jugadores, key=lambda j: j.victorias, reverse=True)
    
    if not jugadores_ordenados:
        return {"mensaje": "No hay jugadores registrados."}

    return {"ranking": [{"nombre": jugador.nombre, "victorias": jugador.victorias} for jugador in jugadores_ordenados]}

@router.delete("/jugadores/{nombre}")
def eliminar_jugador(nombre: str):
    jugador = get_jugador_by_name(nombre)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    jugador.delete_instance()
    return {"mensaje": f"Jugador {nombre} eliminado con éxito"}

@router.get("/jugadores/{nombre}")
def obtener_jugador(nombre: str):
    jugador = get_jugador_by_name(nombre)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return {"nombre": jugador.nombre, "victorias": jugador.victorias, "partidas": jugador.partidas}