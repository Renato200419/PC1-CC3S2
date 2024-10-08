from behave import *
import requests
import re

API_URL = "http://localhost:8000"

def jugador_existe(nombre):
    response = requests.get(f"{API_URL}/jugadores/{nombre}")
    return response.status_code == 200

def partida_existe(partida_id):
    response = requests.get(f"{API_URL}/partidas/{partida_id}")
    return response.status_code == 200

@given('que ingreso un ID de partida válido')
def step_impl(context):
    jugadores = ["Ana", "Luis"]
    for jugador in jugadores:
        if not jugador_existe(jugador):
            response = requests.post(f"{API_URL}/jugadores/", json={"nombre": jugador})
            if response.status_code != 201:
                print(f"Error al registrar jugador {jugador}: {response.status_code}, {response.text}")
    response = requests.post(f"{API_URL}/partidas/", json=[{"nombre": jugadores[0]}, {"nombre": jugadores[1]}]).json()

    # Expresión regular para extraer el ID
    context.partida_id = re.search(r"Partida (\d+) creada con éxito", response["mensaje"]).group(1)

@given('que ingreso un ID de partida inválido')
def step_impl(context):
    context.partida_id = 99999  # Un ID que no debería existir

@given('uno o más jugadores han alcanzado el puntaje máximo')
def step_impl(context):
    jugadores = ["Ana", "Luis"]
    for jugador in jugadores:
        if not jugador_existe(jugador):
            requests.post(f"{API_URL}/jugadores/", json={"nombre": jugador})

    response = requests.post(f"{API_URL}/partidas/", json=[{"nombre": jugadores[0]}, {"nombre": jugadores[1]}]).json()
    # Expresión regular para extraer el ID
    context.partida_id = re.search(r"Partida (\d+) creada con éxito", response["mensaje"]).group(1)

    # Bucle Simulando que los jugadores ya alcanzaron el puntaje máximo
    for _ in range(15):
        response = requests.post(f"{API_URL}/partidas/{context.partida_id}/lanzar")
        if response.status_code not in [200, 201]:
            break

@when('solicito lanzar los dados')
def step_impl(context):
    context.response = requests.post(f"{API_URL}/partidas/{context.partida_id}/lanzar")
    if context.response.status_code not in [200, 201]:
        print(f"Error al lanzar los dados: {context.response.status_code}, {context.response.text}")

@when('se realiza un lanzamiento')
def step_impl(context):
    context.response = requests.post(f"{API_URL}/partidas/{context.partida_id}/lanzar")
    if context.response.status_code not in [200, 201]:
        print(f"Error al realizar el lanzamiento: {context.response.status_code}, {context.response.text}")

@then('el sistema genera números aleatorios entre 1 y 6 para cada jugador')
def step_impl(context):
    assert context.response.status_code in [200, 201]

@then('actualiza y muestra los puntajes acumulados de cada jugador')
def step_impl(context):
    assert context.response.status_code in [200, 201]
    data = context.response.json()
    assert "puntajes" in data, "Los puntajes no están presentes en la respuesta"

@then('el sistema notifica que la partida no existe')
def step_impl(context):
    assert context.response.status_code == 404
    data = context.response.json()
    assert re.search("Partida no encontrada", data["detail"])

@then('no realiza el lanzamiento')
def step_impl(context):
    assert context.response.status_code == 404
    data = context.response.json()
    assert re.search("Partida no encontrada", data["detail"])

@then('el sistema declara al ganador y finaliza la partida')
def step_impl(context):
    response = context.response
    data = response.json()
    expected_message_pattern = r"¡La partida ha terminado! El ganador es (.+) con (\d+) puntos."

    assert re.search(expected_message_pattern, data["mensaje"]), f"Expected message pattern not found in: {data['mensaje']}"
