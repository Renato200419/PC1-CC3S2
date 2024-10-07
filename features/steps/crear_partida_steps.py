from behave import *
import requests
import re

API_URL = "http://localhost:8000"

def jugador_existe(nombre):
    response = requests.get(f"{API_URL}/jugadores/{nombre}")
    return response.status_code == 200

@given('que los jugadores "{jugador1}" y "{jugador2}" están registrados')
def step_impl(context, jugador1, jugador2):
    for jugador in [jugador1, jugador2]:
        if not jugador_existe(jugador):
            requests.post(f"{API_URL}/jugadores/", json={"nombre": jugador})

@given('que el jugador "{jugador}" está registrado')
def step_impl(context, jugador):
    if not jugador_existe(jugador):
        requests.post(f"{API_URL}/jugadores/", json={"nombre": jugador})

@given('que el jugador "{jugador}" no está registrado')
def step_impl(context, jugador):
    if jugador_existe(jugador):
        requests.delete(f"{API_URL}/jugadores/{jugador}")

@when('solicito crear una partida con los jugadores "{jugador1}" y "{jugador2}"')
def step_impl(context, jugador1, jugador2):
    context.response = requests.post(f"{API_URL}/partidas/", json=[{"nombre": jugador1}, {"nombre": jugador2}])

@when('solicito crear una partida con el jugador "{jugador}"')
def step_impl(context, jugador):
    context.response = requests.post(f"{API_URL}/partidas/", json=[{"nombre": jugador}])

@then('el sistema crea la partida asignando un ID único')
def step_impl(context):
    assert context.response.status_code in [200, 201]
    data = context.response.json()
    assert re.search(r"Partida \d+ creada con éxito", data["mensaje"])
    assert re.search(r"'id': \d+", str(data))

@then('confirma que la partida ha sido creada con éxito')
def step_impl(context):
    assert context.response.status_code in [200, 201]

@then('el sistema notifica que el jugador "{jugador}" no está registrado')
def step_impl(context, jugador):
    assert context.response.status_code in [400, 404]
    data = context.response.json()
    assert re.search(f"El jugador '{jugador}' no está registrado", data["detail"])

@then('el sistema notifica que se requieren al menos 2 jugadores')
def step_impl(context):
    assert context.response.status_code == 400
    data = context.response.json()
    assert re.search("Se requieren al menos 2 jugadores", data["detail"])