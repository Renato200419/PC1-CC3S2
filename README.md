# Juego de Dados Competitivo

## Descripción del Proyecto

El **Juego de Dados Competitivo** es una aplicación desarrollada en Python que permite a los jugadores competir en partidas lanzando dados y acumulando puntos. Los jugadores pueden unirse a salas, participar en partidas y ver su posición en el ranking en tiempo real. La aplicación se ejecuta en un entorno contenerizado con Docker y utiliza Prometheus y Grafana para monitorear métricas del juego. Además, el proyecto sigue un flujo DevSecOps que automatiza las pruebas, auditorías de seguridad y despliegues con GitHub Actions.

## Características Principales

- **API REST**: Implementada con FastAPI para gestionar jugadores, partidas y estadísticas.
- **Cliente de Consola (`game_console.py`)**: Interfaz de línea de comandos para que los jugadores se registren, creen partidas, lancen dados y visualicen estadísticas de juego.
- **Monitoreo en Tiempo Real**: Configuración de Prometheus y Grafana para visualizar métricas y estadísticas del juego.
- **DevSecOps Integrado**: Automatización de pruebas, auditoría de seguridad y análisis CI/CD.

## Guía de Instalación y Uso

### Requisitos Previos

- Docker y Docker Compose instalados en el sistema.

### Instalación

1. Clona el repositorio del proyecto:
    ```bash
    git clone https://github.com/Renato200419/PC1-CC3S2.git
    cd PC1-CC3S2
    ```

2. Construye y levanta los servicios utilizando Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Accede a la consola del juego:
    ```bash
    python game_console.py
    ```

### Cómo Jugar

Una vez que accedes a la consola (`game_console.py`), sigue las instrucciones en pantalla para interactuar con el juego. A continuación se detalla el flujo de juego:

1. **Registrar un Jugador**
   - Selecciona la opción `1. Registrar Jugador` e ingresa el nombre del jugador que deseas registrar en el sistema.
   - Ejemplo:
     ```
     Ingresa el nombre del jugador: Juan
     Jugador Juan registrado con éxito.
     ```

2. **Crear una Partida**
   - Selecciona la opción `2. Crear Partida`.
   - Indica el número de jugadores que participarán en la partida.
   - Ingresa los nombres de los jugadores registrados que se unirán a la partida.
   - Ejemplo:
     ```
     Ingresa el número de jugadores: 2
     Ingresa el nombre del jugador: Juan
     Ingresa el nombre del jugador: Ana
     Partida 1 creada con éxito.
     ```

3. **Lanzar Dados**
   - Selecciona la opción `3. Lanzar Dados`.
   - Ingresa el ID de la partida para la cual deseas lanzar los dados.
   - Los jugadores lanzan los dados en su turno y acumulan puntos. Si algún jugador alcanza el puntaje de victoria (por ejemplo, 50 puntos), la partida finaliza y se declara un ganador.
   - Ejemplo:
     ```
     Ingresa el ID de la partida para lanzar los dados: 1
     Lanzando dados......... ¡Listo!
     ¡La partida ha terminado! El ganador es Juan con 50 puntos.
     ```

4. **Mostrar Estadísticas de Partida**
   - Selecciona la opción `4. Mostrar Estadísticas`.
   - Ingresa el ID de la partida de la cual deseas ver las estadísticas y se mostrarán los puntajes acumulados de cada jugador.
   - Ejemplo:
     ```
     Ingresa el ID de la partida para ver estadísticas: 1
     Estadísticas de la partida:
     Puntuaciones: {'Juan': 50, 'Ana': 30}
     ```

5. **Ver el Ranking de Jugadores**
   - Selecciona la opción `5. Mostrar Ranking`.
   - Se mostrará el ranking global de jugadores basado en la cantidad de victorias obtenidas.
   - Ejemplo:
     ```
     === Ranking de Jugadores ===
     1. Juan - 3 victorias
     2. Ana - 2 victorias
     ```

6. **Salir del Juego**
   - Selecciona la opción `6. Salir` para finalizar la ejecución del cliente de consola.

### Monitorización del Juego

Para monitorear las métricas del juego:

1. Accede a la interfaz de Grafana en `http://localhost:3000`.
2. Configura el Data Source en Grafana:
   - En la barra lateral, selecciona Configuration y luego Data Sources.
   - Crea un nuevo Data Source para Prometheus y establece la URL en http://prometheus:9090.
   - Crea un nuevo Data Source para PostgreSQL y se realiza la configuración:
      * **Host URL:** `db:5432`
      * **Database name:** `dadosdb`
      * **Username:** `admin`
      * **Password:** `configured`
      * **TLS/SSL Mode:** `disable`
      * **Version:** `13`
      * **Min time interval:** `1m`
      * **TimescaleDB:** 
      * **Max open connections:** `100`
      * **Auto max idle:**
      * **Max idle connections:** `100`
      * **Max connection lifetime:** `14400`      
   - Guarda la configuración.
3. Importa el dashboard desde la carpeta dashboards/ del proyecto:
   - En Grafana, selecciona la opción Import en la barra lateral.
   - Carga el archivo JSON de la carpeta dashboards/ que contiene la configuración del dashboard.
4. Una vez importado y configurado el Data Source, podrás ver las métricas

## Estructura del Proyecto

- **`app/`**: Implementación de la API REST y lógica del juego.
- **`game_console.py`**: Cliente de consola para interactuar con el juego.
- **`Dockerfile`**: Define la imagen Docker para la aplicación.
- **`docker-compose.yml`**: Archivo de configuración para Docker Compose.
- **`prometheus.yml`**: Configuración de Prometheus para la recolección de métricas.
- **`audit.sh`**: Script para realizar auditorías de seguridad.
- **`Dashboard/`**: Carpeta que contiene el archivo JSON del dashboard de Grafana.
- **`tests/`**: Pruebas unitarias y de integración para asegurar el correcto funcionamiento de la aplicación.
- **`requirements.txt`**: Lista de dependencias de Python para el proyecto.


## Integrantes del Proyecto
- Jorge Alonso Barriga Morales
- Renato Steven Olivera Calderón
- José Ismael Llanos Rosadio

## Contribuciones

Si deseas contribuir a este proyecto:

1. Realiza un fork del repositorio.
2. Crea una nueva rama con las mejoras o correcciones (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza un Pull Request explicando tus cambios.