def jugar_consola():
    print("Bienvenido al Juego de Dados Competitivo")

def mostrar_estadisticas():
    id_partida = int(input("Ingresa el ID de la partida para ver estadísticas: "))
    respuesta = requests.get(f"{API_BASE_URL}/partidas/{id_partida}/estadisticas")
    print("Puntuaciones:", respuesta.json().get('puntajes'))

if __name__ == "__main__":
    jugar_consola()
