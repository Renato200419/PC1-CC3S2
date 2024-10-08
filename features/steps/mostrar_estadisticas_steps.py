from behave import *
import requests
import re

API_URL = "http://localhost:8000"

@given('que existe una partida con ID guardado')
def step_impl(context):
    # Crear jugadores y partida para obtener un ID válido
    jugadores = [{"nombre": "Ana"}, {"nombre": "Luis"}]
    for jugador in jugadores:
        requests.post(f"{API_URL}/jugadores/", json=jugador)
    response = requests.post(f"{API_URL}/partidas/", json=jugadores).json()
    # Expresión regular para extraer el ID
    context.partida_id = re.search(r"Partida (\d+) creada con éxito", response["mensaje"]).group(1)

@given('que no existe una partida con ID "{partida_id}"')
def step_impl(context, partida_id):
    context.partida_id = partida_id

@when('solicito ver las estadísticas de la partida guardada')
def step_impl(context):
    context.response = requests.get(f"{API_URL}/partidas/{context.partida_id}/estadisticas")

@when('solicito ver las estadísticas de la partida con ID "{partida_id}"')
def step_impl(context, partida_id):
    context.response = requests.get(f"{API_URL}/partidas/{partida_id}/estadisticas")

@then('el sistema muestra los puntajes actuales de cada jugador en la partida')
def step_impl(context):
    assert context.response.status_code == 200
    puntajes = context.response.json().get("puntajes")
    assert puntajes is not None

@then('el sistema notifica que la partida no fue encontrada')
def step_impl(context):
    assert context.response.status_code == 404
    mensaje = context.response.json().get("detail")
    assert mensaje == "Partida no encontrada"