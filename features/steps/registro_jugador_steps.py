from behave import *
import requests

API_URL = "http://localhost:8000"

@given('que no existe un jugador con nombre "{nombre}"')
def step_impl(context, nombre):
    requests.delete(f"{API_URL}/jugadores/{nombre}")

@given('que existe un jugador con nombre "{nombre}"')
def step_impl(context, nombre):
    requests.post(f"{API_URL}/jugadores/", json={"nombre": nombre})

@when('solicito registrar el jugador "{nombre}"')
def step_impl(context, nombre):
    context.response = requests.post(f"{API_URL}/jugadores/", json={"nombre": nombre})

@then('el sistema confirma que el jugador ha sido registrado con éxito')
def step_impl(context):
    print(context.response.json())
    assert context.response.status_code == 200

@then('el sistema notifica que el jugador ya está registrado')
def step_impl(context):
    print(context.response.json())
    assert context.response.status_code == 400