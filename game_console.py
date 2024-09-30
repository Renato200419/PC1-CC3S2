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
    #print(respuesta.json().get('mensaje'))
    if respuesta.status_code == 201:
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
        if respuesta.status_code == 201:
            print(Fore.GREEN + respuesta.json().get('mensaje') + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error al crear la partida. Intenta nuevamente." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Número de jugadores inválido, por favor ingresa un número entero." + Style.RESET_ALL)

#def crear_partida():
#    numero_de_jugadores = int(input("Ingresa el número de jugadores: "))
#    jugadores = []
#    for _ in range(numero_de_jugadores):
#        nombre = input("Ingresa el nombre del jugador: ")
#        jugadores.append({"nombre": nombre})
#    respuesta = requests.post(f"{API_BASE_URL}/partidas/", json=jugadores)
#    print(respuesta.json().get('mensaje'))
def lanzamiento_animado():
    """Animación de lanzamiento de dados."""
    print(Fore.YELLOW + "Lanzando dados...", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" ¡Listo!" + Style.RESET_ALL)

def lanzar_dados():
    #id_partida = int(input("Ingresa el ID de la partida para lanzar los dados: "))
    #respuesta = requests.post(f"{API_BASE_URL}/partidas/{id_partida}/lanzar")
    #print(respuesta.json().get('mensaje'))
    #print("Puntuaciones:", respuesta.json().get('puntajes'))
    try:
        id_partida = int(input(Fore.CYAN + "Ingresa el ID de la partida para lanzar los dados: " + Fore.WHITE))
        lanzamiento_animado()
        respuesta = requests.post(f"{API_BASE_URL}/partidas/{id_partida}/lanzar")
        if respuesta.status_code == 200:
            print(Fore.MAGENTA + respuesta.json().get('mensaje') + Style.RESET_ALL)
            print(Fore.CYAN + "Puntuaciones:" + Fore.WHITE, respuesta.json().get('puntajes'))
        else:
            print(Fore.RED + "Error al lanzar los dados. Verifica el ID de la partida." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "ID de la partida inválido, por favor ingresa un número entero." + Style.RESET_ALL)


def mostrar_estadisticas():
    #id_partida = int(input("Ingresa el ID de la partida para ver estadísticas: "))
    #respuesta = requests.get(f"{API_BASE_URL}/partidas/{id_partida}/estadisticas")
    #print("Puntuaciones:", respuesta.json().get('puntajes'))
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
    
#def menu_principal():
    #while True:
    #   print("""
    #    1. Registrar Jugador
    #    2. Crear Partida
    #    3. Lanzar Dados
    #    4. Mostrar Estadísticas
    #    5. Salir
    #    """)
#        opcion = input("Elige una opción: ")
#        if opcion == '1':
#           registrar_jugador()
#        elif opcion == '2':
#            crear_partida()
#        elif opcion == '3':
#            lanzar_dados()
#        elif opcion == '4':
#            mostrar_estadisticas()
#        elif opcion == '5':
#            print("Saliendo del juego. ¡Gracias por jugar!")
#            break
#        else:
#            print("Opción inválida, por favor elige nuevamente.")

#if __name__ == "__main__":
#    menu_principal()

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
        5. Salir
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
            print(Fore.GREEN + "Saliendo del juego. ¡Gracias por jugar!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida, por favor elige nuevamente." + Style.RESET_ALL)

if __name__ == "__main__":
    menu_principal()