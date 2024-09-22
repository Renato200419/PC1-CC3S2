def jugar_consola():
    print("Bienvenido al Juego de Dados Competitivo")

def mostrar_estadisticas():
    id_partida = int(input("Ingresa el ID de la partida para ver estadísticas: "))
    respuesta = requests.get(f"{API_BASE_URL}/partidas/{id_partida}/estadisticas")
    print("Puntuaciones:", respuesta.json().get('puntajes'))

def crear_partida():
    numero_de_jugadores = int(input("Ingresa el número de jugadores: "))
    jugadores = []
    for _ in range(numero_de_jugadores):
        nombre = input("Ingresa el nombre del jugador: ")
        jugadores.append({"nombre": nombre})
    respuesta = requests.post(f"{API_BASE_URL}/partidas/", json=jugadores)
    print(respuesta.json().get('mensaje'))

if __name__ == "__main__":
    jugar_consola()

