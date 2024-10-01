import requests
import time
import random
from colorama import Fore, Style, init

# Inicializar colorama para colores en la consola
init(autoreset=True)

API_BASE_URL = "http://localhost:8000"

def registrar_jugador():
    nombre = input("Ingresa el nombre del jugador: ")
    respuesta = requests.post(f"{API_BASE_URL}/jugadores/", json={"nombre": nombre})
    if respuesta.status_code == 200:
        print(Fore.GREEN + respuesta.json().get('mensaje') + Style.RESET_ALL)
    else:
        print(Fore.RED + "Error al registrar el jugador. Intenta nuevamente." + Style.RESET_ALL)

def crear_partida():
    try:
        numero_de_jugadores = int(input(Fore.CYAN + "Ingresa el número de jugadores: " + Fore.WHITE))
        jugadores = []
        for _ in range(numero_de_jugadores):
            nombre = input(Fore.CYAN + "Ingresa el nombre del jugador: " + Fore.WHITE)
            jugadores.append({"nombre": nombre})
        respuesta = requests.post(f"{API_BASE_URL}/partidas/", json=jugadores)
        if respuesta.status_code == 200:
            print(Fore.GREEN + respuesta.json().get('mensaje') + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error al crear la partida. Intenta nuevamente." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Número de jugadores inválido, por favor ingresa un número entero." + Style.RESET_ALL)

def lanzamiento_animado():
    """Animación de lanzamiento de dados."""
    print(Fore.YELLOW + "Lanzando dados...", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" ¡Listo!" + Style.RESET_ALL)

def lanzar_dados():
    try:
        id_partida = int(input(Fore.CYAN + "Ingresa el ID de la partida para lanzar los dados: " + Fore.WHITE))
        lanzamiento_animado()
        respuesta = requests.post(f"{API_BASE_URL}/partidas/{id_partida}/lanzar")
        if respuesta.status_code == 200:
            mensaje = respuesta.json().get('mensaje')
            puntajes = respuesta.json().get('puntajes')
            cambio_ranking = respuesta.json().get('cambio_ranking', {})

            print(Fore.MAGENTA + mensaje + Style.RESET_ALL)
            print(Fore.CYAN + "Puntuaciones:" + Fore.WHITE, puntajes)

            # Verificar si la partida ha terminado y mostrar el cambio de ranking
            if cambio_ranking:
                print(Fore.YELLOW + "\n=== Cambio de Ranking ===" + Style.RESET_ALL)
                for jugador, posiciones in cambio_ranking.items():
                    print(f"{Fore.CYAN}{jugador}{Style.RESET_ALL}: {posiciones['posicion_inicial']} -> {posiciones['posicion_final']}")
                
        else:
            print(Fore.RED + "Error al lanzar los dados. Verifica el ID de la partida." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "ID de la partida inválido, por favor ingresa un número entero." + Style.RESET_ALL)



def mostrar_estadisticas():
    try:
        id_partida = int(input(Fore.CYAN + "Ingresa el ID de la partida para ver estadísticas: " + Fore.WHITE))
        respuesta = requests.get(f"{API_BASE_URL}/partidas/{id_partida}/estadisticas")
        if respuesta.status_code == 200:
            print(Fore.GREEN + "Estadísticas de la partida:" + Style.RESET_ALL)
            print(Fore.CYAN + "Puntuaciones:" + Fore.WHITE, respuesta.json().get('puntajes'))
        else:
            print(Fore.RED + "Error al obtener las estadísticas. Verifica el ID de la partida." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "ID de la partida inválido, por favor ingresa un número entero." + Style.RESET_ALL)
    
def mostrar_ranking():
    """Función para obtener y mostrar el ranking de jugadores según sus victorias."""
    respuesta = requests.get(f"{API_BASE_URL}/jugadores/ranking/")
    if respuesta.status_code == 200:
        ranking = respuesta.json().get("ranking", [])
        if ranking:
            print(Fore.GREEN + "\n=== Ranking de Jugadores ===" + Style.RESET_ALL)
            for index, jugador in enumerate(ranking, start=1):
                print(f"{index}. {Fore.CYAN}{jugador['nombre']}{Style.RESET_ALL} - {Fore.YELLOW}{jugador['victorias']} victorias{Style.RESET_ALL}")
        else:
            print(Fore.YELLOW + "No hay jugadores registrados en el ranking aún." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Error al obtener el ranking de jugadores." + Style.RESET_ALL)


def menu_principal():
    while True:
        print(Fore.BLUE + """
        ==============================
            Menú Principal del Juego
        ==============================
        1. Registrar Jugador
        2. Crear Partida
        3. Lanzar Dados
        4. Mostrar Estadísticas
        5. Mostrar Ranking
        6. Salir
        """ + Style.RESET_ALL)
        opcion = input(Fore.CYAN + "Elige una opción: " + Fore.WHITE)
        if opcion == '1':
            registrar_jugador()
        elif opcion == '2':
            crear_partida()
        elif opcion == '3':
            lanzar_dados()
        elif opcion == '4':
            mostrar_estadisticas()
        elif opcion == '5':
            mostrar_ranking()  # Se invoca la nueva función mostrar_ranking
        elif opcion == '6':
            print(Fore.GREEN + "Saliendo del juego. ¡Gracias por jugar!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida, por favor elige nuevamente." + Style.RESET_ALL)


if __name__ == "__main__":
    menu_principal()