from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

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

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Juego de Dados"}