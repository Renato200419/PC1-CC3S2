import uvicorn
def jugar_consola():
    print("Bienvenido al Juego de Dados Competitivo")

def crear_partida():
    numero_de_jugadores = int(input("Ingresa el número de jugadores: "))
    jugadores = []
    for _ in range(numero_de_jugadores):
        nombre = input("Ingresa el nombre del jugador: ")
        jugadores.append({"nombre": nombre})
    respuesta = requests.post(f"{API_BASE_URL}/partidas/", json=jugadores)
    print(respuesta.json().get('mensaje'))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    jugar_consola()
