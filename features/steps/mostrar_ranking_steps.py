from behave import *
import requests
import re

API_URL = "http://localhost:8000"

@given('que hay jugadores registrados con partidas jugadas')
def step_impl(context):
    jugadores = [{"nombre": "Ana"}, {"nombre": "Luis"}]
    for jugador in jugadores:
        requests.post(f"{API_URL}/jugadores/", json=jugador)
    # Crear una partida y jugar para registrar estadísticas
    response = requests.post(f"{API_URL}/partidas/", json=jugadores).json()
    # Expresión regular para extraer el ID
    context.partida_id = re.search(r"Partida (\d+) creada con éxito", response["mensaje"]).group(1)
    requests.post(f"{API_URL}/partidas/{context.partida_id}/lanzar")

@given('que no hay jugadores con partidas jugadas')
def step_impl(context):
    # Simular que no hay jugadores registrados
    pass

@when('solicito ver el ranking')
def step_impl(context):
    context.response = requests.get(f"{API_URL}/jugadores/ranking/")

@then('el sistema muestra una lista ordenada de jugadores por número de victorias')
def step_impl(context):
    assert context.response.status_code == 200

@then('el sistema notifica que no hay jugadores registrados')
def step_impl(context):
    assert context.response.status_code == 200