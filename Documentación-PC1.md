# Sobre el documento

Este documento cuenta con un índice para navegar de forma más cómoda. Previo al índice se tienen algunos enlaces de interés para facilitar la revisión del Docente.



# Índice
## 1. Introducción
- [1.1 Descripción del Proyecto](#descripción-del-proyecto)
- [1.2 Objetivos](#objetivos)
- [1.3 Requisitos](#requisitos)

## 2. Desarrollo del Proyecto
- [2.1 Estructura y Arquitectura del Proyecto](#21-estructura-y-arquitectura-del-proyecto)
  - [2.1.1 Descripción General de Archivos y Carpetas](#211-descripción-general-de-archivos-y-carpetas)
  - [2.1.2 Funcionalidad y Propósito de Cada Archivo](#212-funcionalidad-y-propósito-de-cada-archivo)
- [2.2 Estructura de la API REST](#22-estructura-de-la-api-rest)
  - [2.2.1 Propósito](#propósito)
  - [2.2.2 Endpoints de la API](#endpoints-de-la-api)
- [2.3 Explicación de Clases y Almacenamiento de Datos](#23-explicación-de-clases-y-almacenamiento-de-datos)
  - [2.3.1 Clases Definidas en `models.py`](#231-clases-definidas-en-modelspy)
  - [2.3.2 Almacenamiento de Datos](#232-almacenamiento-de-datos)
- [2.4 Dependencias y Librerías Utilizadas](#24-dependencias-y-librerías-utilizadas)
  - [2.4.1 Librerías y su Propósito](#241-librerías-y-su-propósito)
  - [2.4.2 Cómo se Utilizan en el Proyecto](#242-cómo-se-utilizan-en-el-proyecto)
- [2.5 Observabilidad y Monitorización](#25-observabilidad-y-monitorización)
  - [2.5.1 Configuración de Prometheus y Grafana](#251-configuración-de-observabilidad-con-prometheus-y-grafana)
  - [2.5.2 Métricas Monitoreadas](#252-métricas-monitoreadas)
  - [2.5.3 Consultas en Grafana](#253-consultas-en-grafana)
  - [2.5.4 Pasos para Configuración en Grafana y Prometheus](#254-pasos-para-configuración-en-grafana-y-prometheus)
  - [2.5.5 Finalización con Pull Request y Aceptación de Merge](#255-finalización-con-pull-request-y-aceptación-de-merge)
  - [2.2.6 Versión final del Dashboard](#256-versión-final-dashboard-grafana)
- [2.6 Contenerización y Gestión de Servicios](#26-contenerización-y-gestión-de-servicios)
  - [2.6.1 Estructura de los Servicios](#261-estructura-de-los-servicios)
  - [2.6.2 Configuración del Dockerfile y Docker Compose](#262-configuración-del-dockerfile-y-docker-compose)
  - [2.6.3 Ejecución del Proyecto con Docker Compose](#263-ejecución-del-proyecto-con-docker-compose)
  - [2.6.4 Uso de Volúmenes Persistentes](#264-uso-de-volúmenes-persistentes)
  - [2.6.5 Finalización con Pull Request y Aceptación de Merge](#265-finalización-con-pull-request-y-aceptación-de-merge)
- [2.7 Simulación de Partidas Competitivas](#27-simulación-de-partidas-competitivas)
  - [2.7.1 Cliente de Consola para Interacción](#271-cliente-de-consola-para-interacción)
  - [2.7.2 Manejo de Estadísticas](#272-manejo-de-estadísticas)
- [2.8 Planes para la Versión 2.0.0 del Proyecto](#28-planes-para-la-versión-200-del-proyecto)
  - [2.8.1 Descripción General](#281-descripción-general)
  - [2.8.2 Objetivos de la Versión 2.0.0](#282-objetivos-de-la-versión-200)
  - [2.8.3 Cambios en la Estructura de la Aplicación](#283-cambios-en-la-estructura-de-la-aplicación)
  - [2.8.4 Retos y Próximos Pasos](#284-retos-y-próximos-pasos)
  - [2.8.5 Planes Futuros](#28-planes-para-la-versión-200-del-proyecto)
## 3. Gestión del Proyecto con Git
- [3.1 Flujo de Trabajo con GitHub Flow](#31-flujo-de-trabajo-con-github-flow)
  - [3.1.1 Estructura del Flujo de Trabajo](#311-estructura-del-flujo-de-trabajo)
  - [3.1.2 Gráfico de Red (Network Graph)](#312-gráfico-de-red-network-graph)
  - [3.1.3 Ventajas de GitHub Flow](#313-ventajas-de-github-flow)
- [3.2 Resolución de Conflictos con `git mergetool`](#32-resolución-de-conflictos-con-git-mergetool)
- [3.3 Uso de `cherry-pick`](#33-uso-de-cherry-pick)
- [3.4 Revert y Squash](#34-uso-de-revert-y-squash)
- [3.5 Reporte Detallado de Ramas y Commits](#35-reporte-detallado-de-ramas-y-commits)

## 4. DevOps y DevSecOps
- [4.1 Propósito](#41-prop%C3%B3sito)
- [4.2 Pipeline de CI/CD](#42-pipeline-de-cicd)
- [4.3 Configuración de Análisis de Seguridad y Pruebas Automatizadas](#43-configuraci%C3%B3n-de-an%C3%A1lisis-de-seguridad-y-pruebas-automatizadas)
    - [4.3.1 Herramientas de Auditoría](#431-herramientas-de-auditor%C3%ADa)
    - [4.3.2 Ejecución de Auditorías de Seguridad Manuales](#432-ejecuci%C3%B3n-de-auditor%C3%ADas-de-seguridad-manuales)
    - [4.3.3 Reflexión sobre el Impacto de DevOps en el Proyecto](#433-reflexi%C3%B3n-sobre-el-impacto-de-devops-en-el-proyecto)
- [4.4 Reflexión sobre el Flujo de Trabajo DevOps](#44-reflexi%C3%B3n-sobre-el-flujo-de-trabajo-devops)

## 5. Retrospectiva y Aprendizajes
- [5.1 Cambios Introducidos a Partir de la Migración a PostgreSQL](#51-reestructuración-del-proyecto)
- [5.2 Implementación de la Persistencia de Datos con PostgreSQL](#52-implementación-de-la-persistencia-de-datos-con-postgresql)
- [5.3 Monitorización de Tiradas y Puntuaciones con Prometheus](#53-monitorización-de-tiradas-y-puntuaciones-con-prometheus)
- [5.4 Cambios en las Pruebas Automáticas y su Impacto](#54-cambios-en-las-pruebas-automáticas-y-su-impacto)
- [5.5 Reflexión](#55-reflexión-sobre-los-cambios-en-el-proyecto)

## 6. Retrospectiva del Proyecto y Dificultades Encontradas
- [6.1 Dificultades Técnicas](#61-dificultades-técnicas)
- [6.2 Retos en el Trabajo en Equipo](#62-retos-en-el-trabajo-en-equipo)
- [6.3 Retos en la Documentación](#63-retos-en-la-documentación)
- [6.4 Reflexión](#64-reflexión-final)

# 1. Introducción
## Descripción del Proyecto

Desarrollo de un juego de dados competitivo en el que los jugadores compiten por obtener la mayor puntuación a través de lanzamientos de dados. La aplicación cuenta con una API REST para gestionar jugadores y partidas, almacenamiento de datos en PostgreSQL, monitorización de métricas en tiempo real con Prometheus y Grafana, y contenerización con Docker. Además, se implementan prácticas de DevSecOps y pruebas automatizadas para asegurar la calidad y seguridad del proyecto.

---
## Objetivos
 - Implementar una API REST que gestione las partidas y registre las puntuaciones.
 - Desarrollar un cliente de consola para que los jugadores participen en las partidas.
 - Implementar DevSecOps: Configurar un análisis de seguridad específico del lenguaje (pip-audit para Python) y GitHub Actions para CI/CD.
 - Usar Docker y Docker Compose para contenerizar la aplicación y gestionar los servicios.
 - Configurar Prometheus y Grafana para monitorear las métricas del juego, como la cantidad de tiradas y la latencia de la API.
 - Integrar una base de datos relacional PostgreSQL para almacenar las estadísticas de los jugadores y resultados de las partidas.
 - Resolver conflictos de fusión en Git usando git mergetool y documentar el proceso.

---
## Requisitos
- **Lenguaje de Programación**: Python 3.8 o superior.
- **Frameworks y Librerías**: FastAPI para la API REST, Peewee para la integración con PostgreSQL.
- **Base de Datos**: PostgreSQL 13 o superior.
- **Entorno de Contenerización**: Docker y Docker Compose.
- **Monitorización**: Prometheus y Grafana.
- **Control de Versiones**: Git y GitHub para la gestión de ramas y colaboración.
- **Pipelines CI/CD**: Configuración de GitHub Actions para pruebas, integración continua y despliegue.
- **Herramientas de DevSecOp**s: Pip-audit
- **Entorno de Desarrollo**: Visual Studio Code o cualquier IDE compatible con Python y Docker.

---
# 2. Desarrollo del Proyecto

## 2.1 Estructura y Arquitectura del Proyecto

### 2.1.1 Descripción General de Archivos y Carpetas

El proyecto se organiza en diferentes carpetas y archivos que definen su estructura. A continuación, se detalla la estructura del proyecto junto con una breve descripción de cada carpeta:

- **`app/`**: Contiene el código fuente de la aplicación.
  - **`__init__.py`**: Archivo de inicialización del paquete `app`.
  - **`config.py`**: Configuración de la base de datos y otras variables.
  - **`crud.py`**: Operaciones CRUD para interactuar con la base de datos.
  - **`database.py`**: Inicializa la base de datos y crea las tablas necesarias.
  - **`main.py`**: Punto de entrada principal de la aplicación `FastAPI`.
  - **`models.py`**: Definición de los modelos de datos utilizando `Peewee`.
  - **`routes.py`**: Define las rutas de la API para gestionar jugadores, partidas y puntuaciones.

- **`Dashboard/`**: Contiene archivos JSON con las métricas monitoreadas por Prometheus.
- **`Imagenes/`**: Imágenes utilizadas en la documentación.
- **`Imagenes-git/`**: Capturas relacionadas con el uso de Git.
- **`Imagenes-obs/`**: Imágenes relacionadas con la observabilidad del proyecto.
- **`tests/`**: Contiene pruebas unitarias y de integración para el proyecto.
  - **`test_app.py`**: Archivo con las pruebas para validar la API.

- **Archivos principales**:
  - **`README.md`**: Archivo con la descripción general del proyecto.
  - **`Dockerfile`**: Define la imagen Docker para la aplicación.
  - **`docker-compose.yml`**: Define la configuración de los servicios Docker (base de datos, aplicación, Prometheus).
  - **`audit.sh`**: Script para ejecutar auditorías de seguridad en el proyecto.
  - **`requirements.txt`**: Lista de dependencias de Python para el proyecto.

### 2.1.2 Funcionalidad y Propósito de Cada Archivo

A continuación se detalla la funcionalidad de cada archivo dentro de la carpeta `app`:

- **`app/config.py`**: Contiene la configuración de la base de datos PostgreSQL, definiendo el nombre de la base de datos, el usuario, la contraseña y el host. Facilita la conexión con la base de datos para su uso en toda la aplicación.

- **`app/crud.py`**: Implementa las operaciones de acceso a la base de datos, como la creación y obtención de jugadores y partidas, actualización de puntajes y relaciones entre jugadores y partidas.

- **`app/database.py`**: Inicializa la base de datos y crea las tablas necesarias si no existen. Este archivo también incluye funciones para cerrar la conexión de manera segura.

- **`app/main.py`**: Archivo principal para ejecutar la aplicación con `FastAPI` y `uvicorn`. Inicia la API y la instrumentación con Prometheus para monitorear las métricas de la aplicación.

- **`app/models.py`**: Define los modelos de la base de datos usando `Peewee`. Incluye los modelos `Jugador`, `Partida` y `JugadoresPartidas`.

- **`app/routes.py`**: Define las rutas de la API utilizando `FastAPI`. Contiene endpoints para registrar jugadores, crear partidas, lanzar dados y obtener estadísticas de las partidas.

---

## 2.2 Estructura de la API REST

### Propósito

La API permite gestionar partidas y jugadores en un juego de dados competitivo. Los jugadores pueden registrarse, crear partidas, lanzar dados y obtener estadísticas detalladas de las partidas.

### Endpoints de la API

#### 1. **Registrar Jugador**
- **URL**: `/jugadores/`
- **Método**: `POST`
- **Descripción**: Registra un nuevo jugador en el sistema.
- **Solicitud**:
  ```json
  {
    "nombre": "nombre_del_jugador"
  }
  ```
- **Respuesta Exitosa (200)**:
  ```json
  {
    "mensaje": "Jugador nombre_del_jugador registrado con éxito"
  }
  ```
- **Errores**:
  - `400`: El jugador ya está registrado.
  ```json
  {
    "detail": "El jugador ya está registrado"
  }
  ```

#### 2. **Listar Jugadores**
- **URL**: `/jugadores/`
- **Método**: `GET`
- **Descripción**: Lista todos los jugadores registrados en el sistema.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "jugadores": ["nombre_jugador1", "nombre_jugador2"]
  }
  ```
- **Mensaje de Error**:
  - `200`: No hay jugadores registrados.
  ```json
  {
    "mensaje": "No hay jugadores registrados"
  }
  ```

#### 3. **Mostrar Ranking de Jugadores**
- **URL**: `/jugadores/ranking/`
- **Método**: `GET`
- **Descripción**: Muestra el ranking de jugadores basado en el número de victorias.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "ranking": [
      {"nombre": "Juan", "victorias": 3},
      {"nombre": "Ana", "victorias": 2}
    ]
  }
  ```
- **Mensaje de Error**:
  - `200`: No hay jugadores registrados.
  ```json
  {
    "mensaje": "No hay jugadores registrados"
  }
  ```

#### 4. **Crear Partida**
- **URL**: `/partidas/`
- **Método**: `POST`
- **Descripción**: Crea una nueva partida con al menos dos jugadores registrados.
- **Solicitud**:
  ```json
  [
    {"nombre": "jugador1"},
    {"nombre": "jugador2"}
  ]
  ```
- **Respuesta Exitosa (200)**:
  ```json
  {
    "mensaje": "Partida 1 creada con éxito",
    "partida": {"id": 1, "puntajes": {"jugador1": 0, "jugador2": 0}}
  }
  ```
- **Errores**:
  - `400`: Error si hay menos de dos jugadores o si un jugador no está registrado.
  ```json
  {
    "detail": "Se requieren al menos 2 jugadores"
  }
  ```

#### 5. **Lanzar Dados en Partida**
- **URL**: `/partidas/{partida_id}/lanzar`
- **Método**: `POST`
- **Descripción**: Lanza los dados para una partida específica, acumulando los puntos para cada jugador.
- **Parámetros**:
  - `partida_id`: ID de la partida para la cual se lanzarán los dados.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "mensaje": "¡La partida ha terminado! El ganador es Juan con 50 puntos.",
    "puntajes": {"Juan": 50, "Ana": 30},
    "cambio_ranking": {"Juan": {"posicion_inicial": 2, "posicion_final": 1}, "Ana": {"posicion_inicial": 1, "posicion_final": 2}}
  }
  ```
- **Errores**:
  - `404`: Partida no encontrada.
  ```json
  {
    "detail": "Partida no encontrada"
  }
  ```

#### 6. **Obtener Estadísticas de la Partida**
- **URL**: `/partidas/{partida_id}/estadisticas`
- **Método**: `GET`
- **Descripción**: Muestra las estadísticas de una partida específica, incluyendo los puntajes de cada jugador.
- **Parámetros**:
  - `partida_id`: ID de la partida de la cual se desean ver las estadísticas.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "partida_id": 1,
    "puntajes": {"Juan": 50, "Ana": 30}
  }
  ```
- **Errores**:
  - `404`: Partida no encontrada.
  ```json
  {
    "detail": "Partida no encontrada"
  }
  ```

#### 7. **Reiniciar Partida**
- **URL**: `/partidas/{partida_id}/reiniciar`
- **Método**: `POST`
- **Descripción**: Reinicia una partida específica, restableciendo todos los puntajes a cero.
- **Parámetros**:
  - `partida_id`: ID de la partida que se desea reiniciar.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "mensaje": "Partida 1 reiniciada con éxito",
    "puntajes": {"Juan": 0, "Ana": 0}
  }
  ```
- **Errores**:
  - `404`: Partida no encontrada.
  ```json
  {
    "detail": "Partida no encontrada"
  }
  ```

#### 8. **Root**
- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Punto de entrada de la API. Devuelve un mensaje de bienvenida.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "message": "Bienvenido al Juego de Dados"
  }
  ```

---
## 2.3 Explicación de Clases y Almacenamiento de Datos

### 2.3.1 Clases Definidas en `models.py`

- **Jugador**:
  - Representa a un jugador registrado en el sistema.
  - Atributos:
    - `nombre` (str): Nombre único del jugador.
    - `victorias` (int): Número de victorias obtenidas en partidas.
    - `partidas` (int): Número de partidas jugadas.

  Ejemplo de representación:
  ```json
  {
    "nombre": "Juan",
    "victorias": 3,
    "partidas": 10
  }
  ```

- **Partida**:
  - Representa una partida de dados con su ID y puntajes de jugadores.
  - Atributos:
    - `id` (int): Identificador único de la partida.
    - `puntajes` (str): Diccionario en formato string que contiene los puntajes de cada jugador en la partida.

  Ejemplo de representación:
  ```json
  {
    "id": 1,
    "puntajes": "{"Juan": 50, "Ana": 30}"
  }
  ```

- **JugadoresPartidas**:
  - Relaciona a los jugadores con las partidas en las que han participado.
  - Atributos:
    - `jugador` (ForeignKeyField): Referencia al jugador participante.
    - `partida` (ForeignKeyField): Referencia a la partida en la que el jugador ha participado.


### 2.3.2 Almacenamiento de Datos

Los datos se almacenan en una base de datos PostgreSQL configurada en el archivo `config.py`. Se utilizan las siguientes tablas:

- **jugador**: Almacena los datos de los jugadores registrados en el sistema.
- **partida**: Almacena las partidas creadas junto con sus puntajes.
- **jugadores_partidas**: Tabla intermedia que almacena la relación entre jugadores y partidas, permitiendo asociar qué jugadores participaron en qué partidas.

Ejemplo de contenido en la base de datos:
```json
{
  "jugador": [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Pedro"}
  ],
  "partida": [
    {"id": 1, "puntajes": {"Juan": 10, "Pedro": 15}}
  ],
  "jugadores_partidas": [
    {"jugador_id": 1, "partida_id": 1},
    {"jugador_id": 2, "partida_id": 1}
  ]
}
```

---

## 2.4 Dependencias y Librerías Utilizadas

### 2.4.1 Librerías y su Propósito

- **FastAPI**: Framework para construir APIs rápidas y con alto rendimiento, basado en las anotaciones de tipo de Python. Facilita la validación de datos y la creación de rutas.

- **Pydantic**: Se utiliza junto con FastAPI para definir y validar esquemas de datos, como los modelos `Jugador` y `Partida`. Simplifica la gestión de la validación automática.

- **Peewee**: ORM (Object-Relational Mapping) que facilita la interacción con la base de datos PostgreSQL. Permite definir y manipular los modelos `Jugador`, `Partida` y `JugadoresPartidas` de forma sencilla.

- **Prometheus Client (Counter, Histogram)**: Librería que se utiliza para capturar métricas como número de tiradas y latencia de la API.
  - **Counter**: Se usa para contar eventos como la creación de jugadores y partidas.
  - **Histogram**: Se utiliza para medir la latencia de las solicitudes.

- **Prometheus FastAPI Instrumentator**: Instrumenta la API de FastAPI para exponer métricas en el endpoint `/metrics`, permitiendo su monitoreo con Prometheus y Grafana.

- **Uvicorn**: Servidor ASGI para ejecutar aplicaciones construidas con FastAPI. Permite servir la API localmente y monitorear las solicitudes.

### 2.4.2 Cómo se Utilizan en el Proyecto

Cada librería tiene un rol específico en el proyecto:

- `FastAPI` y `Pydantic` se encargan del manejo de las rutas, validación de datos y gestión de solicitudes y respuestas.
- `Peewee` maneja la interacción con la base de datos, incluyendo la creación de tablas y operaciones CRUD.
- `Prometheus Client` y `Prometheus FastAPI Instrumentator` se utilizan para monitorear la API y capturar métricas que luego se visualizan en `Grafana`.
- `Uvicorn` facilita la ejecución de la aplicación y su despliegue local para desarrollo y pruebas.


---

## 2.5 Observabilidad y Monitorización

En esta sección se describe cómo se ha configurado y utilizado Prometheus y Grafana para monitorizar el rendimiento y comportamiento de la API del juego de dados. La integración de estas herramientas permite recolectar y visualizar métricas personalizadas, facilitando la identificación de problemas de latencia y el monitoreo de eventos en tiempo real.

### 2.5.1 Configuración de Observabilidad con Prometheus y Grafana

#### Introducción

En este proyecto, se utiliza Prometheus para recolectar métricas de la API REST del juego de dados y Grafana para visualizar esas métricas. La monitorización nos permite rastrear el comportamiento de la API y detectar posibles problemas de rendimiento o errores, como latencia alta o un número inesperado de tiradas de dados.

#### Configuración de Prometheus

El archivo `prometheus.yml` contiene la configuración para que Prometheus recolecte las métricas de la API del juego.

##### Archivo `prometheus.yml`:
```yaml
global:
  scrape_interval: 15s  # Frecuencia con la que Prometheus recopila las métricas

scrape_configs:
  - job_name: 'py-app'  # Nombre del trabajo de monitoreo
    static_configs:
      - targets: ['app:8000']  # API del juego ejecutándose en el puerto 8000
```
Para acceder a Prometheus, dirígete a [http://localhost:9090](http://localhost:9090).

#### Configuración de Grafana

Grafana se utiliza para visualizar las métricas recolectadas por Prometheus. Hemos configurado varios dashboards que muestran información clave sobre la aplicación.

**Importación de Dashboards:**
- Los dashboards preconfigurados están en la carpeta `metrics_dashboards/`.
- Para importar un dashboard en Grafana:
  1. Acceder a Grafana en [http://localhost:3000](http://localhost:3000).
  2. Ir a `Dashboards` > `Manage` > `Import`.
  3. Seleccionar el archivo JSON desde `metrics_dashboards/` y seguir las instrucciones para configurar la fuente de datos.

2.5.2 **Métricas Monitoreadas**

Se están monitoreando varias métricas clave del juego de dados y del rendimiento de la API utilizando Prometheus. Cada métrica personalizada se utiliza para monitorear aspectos específicos del juego:

#### **Métricas Personalizadas**

- **`jugadores_counter`**:  
  - **Descripción**: Contador que registra el número total de jugadores que se han unido al juego.  
  - **Propósito**: Ayuda a monitorear cuántos jugadores han sido registrados exitosamente en el sistema.
  
- **`partidas_counter`**:  
  - **Descripción**: Contador que registra el número total de partidas creadas en el sistema.  
  - **Propósito**: Permite realizar un seguimiento del número de partidas iniciadas, ayudando a identificar la actividad en el juego.

- **`tiradas_counter`**:  
  - **Descripción**: Contador que registra el número total de tiradas de dados realizadas en el juego.  
  - **Propósito**: Proporciona información sobre la cantidad de acciones realizadas por los jugadores, permitiendo evaluar la interacción en las partidas.

- **`latencia_histogram`**:  
  - **Descripción**: Histograma que mide la latencia de las solicitudes a la API REST en segundos.  
  - **Propósito**: Permite monitorear el rendimiento de la API y detectar posibles problemas de respuesta en las solicitudes.

- **`puntuaciones_altas_counter`**:  
  - **Descripción**: Contador que registra el número total de veces que se ha obtenido una puntuación alta (valor 6) en el lanzamiento de dados.  
  - **Propósito**: Facilita el análisis de cuántas veces los jugadores logran obtener el valor máximo, lo que puede ayudar a entender la distribución de resultados y validar la aleatoriedad de los lanzamientos.

#### **Ejemplo de Código para las Métricas en la API**

En la implementación de la API REST se utilizan las siguientes métricas de Prometheus:

```python
# Métricas de Prometheus
jugadores_counter = Counter("jugadores_registrados_totales", "Total de jugadores registrados")
partidas_counter = Counter("partidas_creadas_totales", "Total de partidas creadas")
tiradas_counter = Counter("tiradas_totales", "Total de tiradas realizadas")
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")
puntuaciones_altas_counter = Counter("puntuaciones_altas", "Total de veces que se han obtenido puntuaciones altas (número 6)")
```

Estas métricas se utilizan dentro de los endpoints para monitorear en tiempo real el comportamiento de la API y las acciones realizadas por los jugadores.


### 2.5.3 Consultas en Grafana

A continuación se muestran algunas consultas comunes que se pueden utilizar en Grafana para visualizar las métricas recolectadas por Prometheus.

#### Tiradas Totales (`tiradas_totales_total`)

Consulta para visualizar el número total de tiradas de dados en el último minuto:

```promql
increase(tiradas_totales_total[1m])
```

#### Latencia de la API (`latencia_api`)

Consulta para ver la latencia promedio de la API:

```promql
rate(latencia_api_sum[1m]) / rate(latencia_api_count[1m])
```

### 2.5.4 Pasos para Configuración en Grafana y Prometheus

1. Luego de usar el comando: `docker-compose up --build -d`, abrimos el enlace: [http://localhost:3000] y nos logeamos como: `admin` tanto en usuario como contraseña.
   ![Descripción de la imagen](Imagenes-obs/Foto1_.png)
2. De igual manera, ingresamos al enlace de Prometheus: 
   ![Descripción de la imagen](Imagenes-obs/Foto2.png)
3. Estando en Grafana nos dirigimos a `Dashboards` y configuramos una nueva `data source` que en este caso sería Prometheus. Lo configuramos así:
   ![Descripción de la imagen](Imagenes-obs/Foto3.png)
   ![Descripción de la imagen](Imagenes-obs/Foto4.png)
   ![Descripción de la imagen](Imagenes-obs/Foto5.png)
4. Importamos un dashboard llamado "Métricas" y luego agregamos un query para el panel "Latencia".
   ![Descripción de la imagen](Imagenes-obs/Foto6.png)
5. Luego se duplicó el panel, y esta vez lo configuramos llamándolo: "Tiradas_totales".
   ![Descripción de la imagen](Imagenes-obs/Foto7.png)
6. Entonces, en `main.py` se jugaría una partida y se tirarían los dados. Finalmente, vemos los cambios reflejados en los dashboards.
   ![Descripción de la imagen](Imagenes-obs/Foto8.png)
   ![Descripción de la imagen](Imagenes-obs/Foto9.png)
7. También se pudo visualizar en Prometheus, dando clic en `open metrics explorer` y luego ejecutando la consulta.
   ![Descripción de la imagen](Imagenes-obs/Foto10.png)
8. Para finalizar, se importó el dashboard y se agregó a la rama.

### 2.5.5 Finalización con Pull Request y Aceptación de Merge

1. Al subir los cambios en la rama, se hace un `Compare & pull request`.
2. Se añade un título y una descripción breve.
3. Luego se agrega un comentario indicando que estás esperando la aceptación de los cambios. (opcional)
4. Uno de los colaboradores acepta los cambios y se realiza el `merge`.

   ![Descripción de la imagen](Imagenes-obs/Foto11.png)

### 2.5.6 Versión final Dashboard Grafana

1. En Grafana configuramos un `data source` nuevo para nuestro **Dashboard final**. Se trata de postgreSQL

    ![sql](Imagenes-obs/psql.png)

2. Configuramos un nuevo panel para el top 5 según cantidad de victorias

    ![tabla](Imagenes-obs/tabla.png)

3. Añadimos más paneles con las métricas implementadas en nuestra versión final y observamos el resultado:

   ![dashboard](Imagenes-obs/dashboard.png) 

--- 

## 2.6 Contenerización y Gestión de Servicios

En esta sección se describe cómo se ha configurado la contenerización de la aplicación del juego de dados y sus servicios asociados utilizando Docker y Docker Compose, junto con la base de datos PostgreSQL. Se explica cómo se ha construido la imagen de la aplicación, cómo se han orquestado los servicios mediante Docker Compose y cómo se ha integrado PostgreSQL para la persistencia de datos. Además, se detalla la inclusión de servicios adicionales como Prometheus y Grafana para la monitorización y visualización de métricas en tiempo real.

### 2.6.1 Estructura de los Servicios

El proyecto contiene los siguientes servicios dentro de contenedores:

- **app**: Contenedor que ejecuta la API REST del juego de dados desarrollada en Python usando FastAPI.
- **postgresql**: Contenedor que aloja la base de datos PostgreSQL para almacenar las estadísticas de los jugadores y resultados de las partidas.
- **prometheus**: Contenedor que ejecuta Prometheus para recolectar métricas de la API.
- **grafana**: Contenedor que ejecuta Grafana para visualizar las métricas recolectadas por Prometheus.

### 2.6.2 Configuración del Dockerfile y Docker Compose

#### Dockerfile

En el repositorio se creó la rama `feature/metrics-and-endpoints`, en la cual se agregó el Dockerfile:

```dockerfile
# Usamos la imagen base de Python 3.8
FROM python:3.8
# Crear directorio de la app y copiar todo el contenido
WORKDIR /app
# Copiar el contenido del directorio actual a /app en el contenedor
COPY . /app
# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Exponer el puerto
EXPOSE 8000
# Ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

#### docker-compose.yml

El archivo `docker-compose.yml` orquesta la ejecución de todos los servicios necesarios, incluyendo la configuración de la base de datos PostgreSQL, así como la integración de Prometheus y Grafana:

```yaml
version: '3.8'  # Usa la versión 3.8 de Docker Compose
services:
  app:  # Nombre del servicio
    build: .  # Construye la imagen a partir del Dockerfile en el directorio actual
    ports:
      - "8000:8000"  # Mapea el puerto 8000 del contenedor al puerto 8000 del host
    depends_on:
      - db  # Asegura que el servicio de base de datos PostgreSQL esté en ejecución antes de iniciar la app
    environment:
      - DATABASE_URL=postgresql://admin:secret@db:5432/dadosdb  # Configurar la URL de la base de datos
    volumes:
      - .:/app  # Monta el directorio actual en /app dentro del contenedor

  db:
    image: postgres:13  # Usa la imagen oficial de PostgreSQL
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: dadosdb
    ports:
      - "5432:5432"  # Mapea el puerto 5432 del contenedor al puerto 5432 del host
    volumes:
      - postgres_data:/var/lib/postgresql/data  # Define un volumen para la persistencia de datos

  prometheus:
    image: prom/prometheus  # Utiliza la imagen oficial de Prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml  # Monta el archivo de configuración de Prometheus
      - prometheus_data:/prometheus  # Persistencia de datos de Prometheus
    ports:
      - "9090:9090"  # Mapea el puerto 9090 del contenedor al puerto 9090 del host
    depends_on:
      - app  # Asegura que el servicio 'app' esté en ejecución antes de iniciar Prometheus

  grafana:
    image: grafana/grafana  # Utiliza la imagen oficial de Grafana
    volumes:
      - grafana_data:/var/lib/grafana  # Persiste datos de Grafana aquí
    ports:
      - "3000:3000"  # Mapea el puerto 3000 del contenedor al puerto 3000 del host
    depends_on:
      - prometheus  # Asegura que Prometheus esté en ejecución antes de iniciar Grafana
    environment:
      - GF_USERS_ALLOW_SIGN_UP=false  # Desactiva el registro de nuevos usuarios

volumes:
  postgres_data:  # Volumen para persistir los datos de PostgreSQL
  grafana_data:  # Volumen para persistir los datos de Grafana
  prometheus_data:  # Volumen para persistir los datos de Prometheus
```

#### Dependencias en `requirements.txt`

Se actualizó `requirements.txt` para agregar dependencias necesarias (`fastapi`, `uvicorn`, `prometheus_client`) y herramientas de seguridad (`pip-audit`) y pruebas (`pytest`). Esto asegura la correcta instalación en el contenedor Docker y en CI/CD.

```bash
fastapi~=0.115.0
uvicorn~=0.22.0
pydantic~=2.9.2
pip-audit
pytest
httpx

prometheus_client~=0.21.0
prometheus-fastapi-instrumentator
requests~=2.32.3

peewee~=3.17.6
psycopg2-binary==2.9.6
```

### 2.6.3 Ejecución del Proyecto con Docker Compose

#### Iniciar los Servicios

Para iniciar todos los servicios (API, Prometheus y Grafana), ejecutar el siguiente comando:

```bash
docker-compose up --build
```

#### Detener los Servicios

Para detener todos los servicios, usar:

```bash
docker-compose down
```

#### Reconstruir los Contenedores

Si se realizan cambios en el código o en las configuraciones, se deben reconstruir los contenedores utilizando el siguiente comando:

```bash
docker-compose up --build
```

#### Verificar los Contenedores Corriendo

Para verificar que todos los contenedores están en ejecución, ejecutar:

```bash
docker ps
```

### 2.6.4 Uso de Volúmenes Persistentes

Para asegurar que los datos de Grafana y Prometheus no se pierdan entre reinicios de contenedores, se configuraron los siguientes volúmenes:

- **Volumen de Grafana (`grafana_data`)**: Almacena dashboards y configuraciones de Grafana.
- **Volumen de Prometheus (`prometheus_data`)**: Almacena datos históricos de métricas recolectadas por Prometheus.
- **Volumen de PostgreSQL (`postgres_data`)**: Se utiliza para almacenar la base de datos y las tablas de la aplicación.

```yaml
volumes:
  grafana_data:  # Almacena datos de Grafana
  prometheus_data:  # Almacena datos de Prometheus
  postgres_data:  # Almacena datos de PostgreSQL
```

### 2.6.5 Finalización con Pull Request y Aceptación de Merge

1. Al subir los cambios en la rama, se hace un `Compare & pull request`.
2. Se añade un título y una descripción breve.
3. Luego se agrega un comentario avisando que se está esperando la aceptación de los cambios (opcional).
4. Uno de los colaboradores acepta los cambios y se realiza el `merge`.

   ![Descripción de la imagen](Imagenes/Imagen.png)

---
## **2.7 Cliente de Consola**

### **2.7.1 Descripción General**

El cliente de consola permite a los usuarios interactuar con el juego de dados a través de comandos de texto. Utiliza la API para registrar jugadores, crear partidas, lanzar dados, consultar estadísticas de las partidas y visualizar el ranking de jugadores. La interfaz ha sido diseñada para ser intuitiva y proporcionar una experiencia agradable mediante el uso de colores.

### **2.7.2 Funcionalidades del Cliente de Consola**

1. **Registrar Jugador**
    - El usuario ingresa el nombre del jugador y el cliente realiza una solicitud `POST` a la ruta `/jugadores/` de la API para registrar al jugador en el sistema.
    - Si el registro es exitoso, se muestra un mensaje de confirmación en verde. En caso de error, se muestra un mensaje en rojo indicando que el jugador ya está registrado.

2. **Crear Partida**
    - El cliente solicita al usuario que ingrese el número de jugadores y luego los nombres de cada uno. 
    - Se realiza una solicitud `POST` a la ruta `/partidas/` de la API para crear la partida.
    - Si la partida se crea con éxito, se muestra un mensaje con el ID de la partida. Si ocurre un error, se informa al usuario.

3. **Lanzar Dados**
    - El usuario ingresa el ID de la partida para la cual se desean lanzar los dados. 
    - El cliente realiza una solicitud `POST` a la ruta `/partidas/{partida_id}/lanzar`.
    - Una vez lanzados los dados, se muestra una animación en la consola y se presentan los puntajes acumulados de cada jugador.
    - Si se alcanza el puntaje de victoria (por ejemplo, 50 puntos), la partida finaliza y se declara un ganador. También se muestra el cambio en la posición de ranking de los jugadores involucrados en la partida.

4. **Mostrar Estadísticas**
    - El usuario ingresa el ID de la partida para la cual desea ver las estadísticas.
    - El cliente realiza una solicitud `GET` a la ruta `/partidas/{partida_id}/estadisticas` para obtener los puntajes de cada jugador en la partida.
    - Se muestran los puntajes actuales de todos los jugadores.

5. **Mostrar Ranking**
    - El cliente realiza una solicitud `GET` a la ruta `/jugadores/ranking/` para obtener el ranking de jugadores basado en el número de victorias.
    - Los jugadores se listan de acuerdo a sus victorias en orden descendente. Si no hay jugadores registrados, se muestra un mensaje informativo.

6. **Salir**
    - Permite al usuario salir del juego y finalizar la ejecución del cliente de consola.

### **2.7.3 Estructura de las Funciones**

A continuación se describen las principales funciones implementadas en el cliente de consola:

- **`registrar_jugador()`**: Registra un nuevo jugador solicitando el nombre y utilizando la API. Muestra mensajes en la consola indicando el éxito o el fallo del registro.

- **`crear_partida()`**: Crea una nueva partida con los jugadores indicados. Solicita el número de jugadores y los nombres de cada uno antes de enviar la solicitud a la API.

- **`lanzamiento_animado()`**: Muestra una animación de lanzamiento de dados en la consola para hacer la experiencia más visual.

- **`lanzar_dados()`**: Lanza los dados para una partida específica. Solicita el ID de la partida, muestra los puntajes acumulados y, si la partida ha terminado, muestra el cambio de ranking de los jugadores.

- **`mostrar_estadisticas()`**: Muestra las estadísticas de una partida específica, incluyendo los puntajes de cada jugador.

- **`mostrar_ranking()`**: Muestra el ranking global de jugadores basado en el número de victorias.

- **`menu_principal()`**: Muestra el menú principal del juego con las opciones disponibles y gestiona la navegación entre las funciones del cliente.

### **2.7.4 Ejemplo de Uso del Cliente de Consola**

A continuación se muestra un ejemplo de uso del cliente de consola:

```bash
==============================
    Menú Principal del Juego
==============================
1. Registrar Jugador
2. Crear Partida
3. Lanzar Dados
4. Mostrar Estadísticas
5. Mostrar Ranking
6. Salir

Elige una opción: 3
Ingresa el ID de la partida para lanzar los dados: 1
Lanzando dados...D...D...D ¡Listo!
¡La partida ha terminado! El ganador es Juan con 50 puntos.
Puntuaciones: {'Juan': 50, 'Ana': 30}
=== ¡Cambios en la Clasificación! ===
Juan: 2 -> 1
Ana: 1 -> 2
```

---
### **2.8 Planes para la Versión 2.0.0 del Proyecto**

#### **2.8.1 Descripción General**

La versión 2.0.0 del proyecto de juego de dados competitivo se centra en la transición de la aplicación a un sistema cliente-servidor para permitir una experiencia multijugador real. Esta nueva versión se diseñará para ofrecer una mayor independencia a cada jugador durante el transcurso de las partidas, así como mejorar la gestión de partidas y la interactividad del juego.

#### **2.8.2 Objetivos de la Versión 2.0.0**

1. **Implementar la Consola de Jugadores:**
   - En esta versión, se separará la consola de administración actual (`game_console.py`) de la consola de jugadores, creando una nueva consola destinada exclusivamente a las interacciones de los jugadores.
   - Los jugadores podrán registrarse, crear y unirse a salas, y participar en partidas de forma independiente.

2. **Estructura de Salas y Partidas:**
   - Las partidas no se iniciarán de inmediato cuando los jugadores se unan. En su lugar, se crearán salas de espera donde los jugadores se podrán unir hasta alcanzar el número máximo configurado para cada partida.
   - Una vez que una sala alcanza el número máximo de jugadores, la partida se iniciará automáticamente, permitiendo a los jugadores competir con un flujo de juego más dinámico y ordenado.

3. **Modos de Juego:**
   - En esta versión, se planea incluir configuraciones para diferentes modos de juego. El modo "Competitivo" será el primero en implementarse, pero se tiene contemplado explorar otros modos, como "Cooperativo" y "Eliminación Directa", en futuras actualizaciones.
   - En los nuevos modos de juego también se planea incluir la opción de activar modificadores especiales en la partida, algunos ejemplos son: "Puntuaciones dobles", donde los jugadores pueden elegir en qué turno activar un multiplicador de puntos; "Robo de puntos", que activa la habilidad de robarle los puntos a un jugador en el turno actual; "Intercambio de puntos", que intercambia el puntaje que obtienen dos jugadores en un turno; entre otros.

4. **Límites de Tiempo por Turno:**
   - Se establecerá un límite de tiempo por turno (15 segundos), lo cual añade un componente estratégico a la toma de decisiones en cada lanzamiento de dados. Los jugadores deberán pensar rápidamente y actuar antes de que se agote el tiempo.

5. **Integración de Métricas de Monitoreo:**
   - Continuar con la integración de Prometheus y Grafana para monitorear el rendimiento y la actividad de la API en tiempo real. Se añadirán nuevas métricas como:
     - *Tiempo de respuesta promedio por solicitud de jugador.*
     - *Número de jugadores activos en salas.*
     - *Cantidad de partidas finalizadas exitosamente.*

#### **2.8.3 Cambios en la Estructura de la Aplicación**

- **Endpoints y Funcionalidades:**
  - Los endpoints de la API se mantendrán, pero se realizarán ajustes para soportar la nueva estructura de salas y turnos. Se espera añadir rutas adicionales para gestionar la creación y eliminación de salas, así como la administración de los turnos de cada jugador.

- **Modelo de Datos:**
  - Se contempla la incorporación de un nuevo modelo llamado `Sala` para gestionar la información de cada sala de espera y su asociación con los jugadores.

- **Interacción en la Consola:**
  - La consola de jugadores ofrecerá un menú interactivo con opciones para:
    - *Registrarse o iniciar sesión.*
    - *Unirse a salas existentes o crear nuevas salas.*
    - *Participar en partidas, visualizando su turno y lanzando los dados cuando sea su turno.*
  - Los jugadores recibirán mensajes en la consola informando sobre los cambios en la sala, como la entrada de nuevos jugadores o el inicio de la partida.

---

# 3. Gestión del Proyecto con Git

## 3.1 Flujo de Trabajo con GitHub Flow

### 3.1.1 Estructura del Flujo de Trabajo

El proyecto sigue el GitHub Flow, un flujo de trabajo ligero y flexible que facilita el desarrollo colaborativo y continuo. GitHub Flow se basa en ramas (`branches`) y Pull Requests (PRs) para gestionar el ciclo de vida de las características y correcciones de errores de manera eficiente.

El flujo de trabajo seguido en este proyecto tiene los siguientes pasos:

1. **Rama Principal (main)**:
   - La rama `main` siempre contiene el código estable y listo para producción.
   - Todos los cambios nuevos deben pasar por una revisión antes de fusionarse en `main`.

2. **Crear una Rama de Funcionalidad (Feature Branch)**:
   - Cada nueva funcionalidad o corrección se desarrolla en su propia rama.
   - Para empezar a trabajar en una nueva funcionalidad, primero se crea una nueva rama desde `main`:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
   ![Descripción de la imagen](Imagenes-git/Foto1.png)

3. **Hacer Commits en la Nueva Rama**:
   Se realizan commits pequeños y significativos a medida que se desarrolla la nueva funcionalidad o la corrección de errores:
   ```bash
   git add .
   git commit -m "Se implementa la nueva funcionalidad X"
   ```
   ![Descripción de la imagen](Imagenes-git/Foto2.png)

4. **Abrir un Pull Request (PR)**:
   - Una vez que la nueva funcionalidad esté lista, abrimos un PR desde la rama que se ha creado hacia `main`.
   - Agregamos una descripción breve junto con su título.
   - Esto permite que otros miembros del equipo revisen los cambios antes de fusionarlos.
   ![Descripción de la imagen](Imagenes-git/Foto3.png)
   ![Descripción de la imagen](Imagenes-git/Foto4.png)

5. **Revisión y Fusión (Merge)**:
   - El PR debe ser revisado por al menos un colaborador.
   - Después de ser aprobado y si no hay conflictos, el PR se fusiona en `main`.
   ![Descripción de la imagen](Imagenes-git/Foto5.png)

   **Resultado Final**:
   ![Descripción de la imagen](Imagenes-git/Foto6.png)

6. **Despliegue a Producción**:
   Como `main` siempre contiene código listo para producción, cualquier cambio fusionado en `main` puede ser desplegado inmediatamente.

### 3.1.2 Gráfico de Red (Network Graph)

El siguiente gráfico muestra cómo se ha desarrollado el proyecto utilizando GitHub Flow, con múltiples ramas de funcionalidad y fusiones (Pull Requests) en la rama `main`.

![Descripción de la imagen](Imagenes-git/Foto7.png)

Cada línea representa una rama de funcionalidad o corrección de errores que se desarrolló de manera independiente antes de fusionarse en `main`.
Los puntos representan commits realizados a lo largo del tiempo, mientras que los bloques de fusión muestran cuándo las ramas fueron fusionadas en `main`.

### 3.1.3 Ventajas de GitHub Flow

GitHub Flow es ideal para este proyecto porque:

- **Flujo ligero**: Es simple y fácil de seguir, adecuado para un ciclo de desarrollo continuo.
- **Despliegue frecuente**: Permite despliegues frecuentes, ya que cualquier cambio en `main` está listo para producción.
- **Revisión colaborativa**: Los Pull Requests facilitan la colaboración y aseguran que el código sea revisado antes de ser fusionado.

## 3.2 Resolución de Conflictos con `git mergetool`

En ocasiones, dos o más desarrolladores pueden trabajar en partes similares del código, lo que provoca conflictos de fusión. Para resolver estos conflictos se usó `git mergetool`. A continuación se muestra un ejemplo detallado:

1. A partir de la rama `main`, se creó la rama `feature/interfaz` y luego se crearon dos ramas a partir de esa rama:
2. El colaborador A crea la rama `feature/interfaz-crear_partida` a partir de `feature/interfaz`. Luego realiza cambios agregando la función `crear_partida` en `main.py`.
   ![Descripción de la imagen](Imagenes-git/Foto8.png)

3. El colaborador B crea la rama `feature/interfaz-mostrar_estadisticas` a partir de `feature/interfaz`. Luego realiza cambios agregando la función `mostrar_estadisticas` en `main.py`.
   ![Descripción de la imagen](Imagenes-git/Foto9.png)

4. Luego de que cada colaborador hace un `git push origin <nombre de la rama respectiva>`, el colaborador A crea un Pull Request y lo envía para revisión.
   ![Descripción de la imagen](Imagenes-git/Foto10.png)
   ![Descripción de la imagen](Imagenes-git/Foto11.png)

5. El colaborador B acepta el PR y se realiza la fusión.
   ![Descripción de la imagen](Imagenes-git/Foto12.png)
   ![Descripción de la imagen](Imagenes-git/Foto13.png)

6. Ahora el colaborador B intenta realizar un PR y se encuentra con un conflicto de fusión.
   ![Descripción de la imagen](Imagenes-git/Foto14.png)

7. El colaborador B actualiza su rama `feature/interfaz` con los últimos cambios de `main` y se encuentra con el conflicto.
   ![Descripción de la imagen](Imagenes-git/Foto15.png)

8. Para resolverlo, usa el comando `git mergetool`, que abrirá Visual Studio Code para resolver el conflicto de manera visual.
   ![Descripción de la imagen](Imagenes-git/Foto16.png)
   ![Descripción de la imagen](Imagenes-git/Foto17.png)

9. El colaborador B soluciona el conflicto uniendo ambos cambios y realiza el commit y push correspondientes.
   ![Descripción de la imagen](Imagenes-git/Foto18.png)
   ![Descripción de la imagen](Imagenes-git/Foto19.png)

10. Finalmente, el colaborador A acepta el PR y se realiza la fusión con éxito.
   ![Descripción de la imagen](Imagenes-git/Foto20.png)
   ![Descripción de la imagen](Imagenes-git/Foto21.png)
   ![Descripción de la imagen](Imagenes-git/Foto22.png)

## 3.3 Uso de Cherry-pick

La situación que enfrentamos para utilizar `cherry-pick` fue la siguiente:

1. **Creación de Ramas**:  
   Se creó la rama `feature/metrics` para configurar las métricas de Prometheus. En un momento, se vio la necesidad de actualizar el Dockerfile para cambiar la forma en la que se instalaban las dependencias, por lo que se creó una rama adicional a partir de `feature/metrics` llamada `feature/metrics-docker-update`.

2. **Creación y Fusión de PR**:  
   Al terminar los cambios en `feature/metrics-docker-update`, se procedió a crear una Pull Request (PR) y fusionar.

   ![Descripción de la imagen](Imagenes-git/PR17.png)

3. **Error de Fusión Detectado**:  
   Se detectó un error, ya que la PR solicitaba fusionar `feature/metrics-docker-update` con `main`. Al darnos cuenta del error, creamos otra PR realizando la fusión correcta de `feature/metrics-docker-update` a `feature/metrics` y, posteriormente, se fusiona `feature/metrics` con `main`.

   ![Descripción de la imagen](Imagenes-git/PR18.png)
   ![Descripción de la imagen](Imagenes-git/PR19.png)

4. **Reversión del Merge Erróneo**:  
   Luego de estas PR, se procedió a revertir el merge de `feature/metrics-docker-update` con `main`. El problema ocurrió porque al revertir la PR 17 (el merge erróneo) después de aceptar las PR-18 y PR-19, se eliminaron cambios que ya no se incluían en las últimas PR porque se suponía que habían sido incluidos antes.

5. **Uso de Cherry-pick para Solucionar el Problema**:  
   La rama `main` quedó sin varios commits relevantes. Una solución rápida fue utilizar `cherry-pick` para traer esos cambios de nuevo a `main`. A continuación, se muestra la PR que resolvió el problema:

   ![Descripción de la imagen](Imagenes-git/PR20.png)

6. **Problema con el Pipeline Detectado**:  
   El integrante Olivera se dio cuenta de un problema con nuestro Pipeline tras traer estos commits:

   ![Descripción de la imagen](Imagenes-git/Problema.png)

7. **Revisión y Solución del Problema**:  
   El integrante Barriga leyó el comentario y, tras analizar la causa de que la API no respondiera, se dio cuenta de que faltaba hacer un `cherry-pick` de un commit más. Se realizaron los cambios y se aprobó la PR, logrando que la API funcionara correctamente.

   ![Descripción de la imagen](Imagenes-git/solucion.png)

8. **Revisión del Gráfico de Ramas**:  
   Con esto, nuestro gráfico de las ramas se ve de la siguiente manera:

   ![Descripción de la imagen](Imagenes-git/branches.png)

## 3.4 Uso de Revert y Squash

Un caso donde requerimos el uso de `git revert` y `git squash` fue en la PR #46 que fue una de las más desafiantes para el equipo, pues el cambio a usar almacenamiento con una base de datos rompía importaciones entre archivos, endpoints y el flujo del pipeline CI/CD.

La situación presentada fue la siguiente:
- El compañero Barriga realizar un commit en una rama y crea la PR

	![PR46](Imagenes/PR46.png)
- Intenta solucionar el error en el pipeline CI/CD y solicita apoyo del compañero Olivera

	![PR46-commits](Imagenes/PR-46-commits.png)
- El compañero Barriga nota que hay algunos cambios que empeoran la situación así que decide hacer revert paso a paso hasta una versión más estable (aún defectuosa), para ello se hace `git revert` sucesivamente y finalmente se hace `squash` para mantener el historial de commits limpio

	![revert-squash](Imagenes/revert-squash.png)

Finalmente, se logró solucionar el problema y estabilizar la aplicación, aunque no se detallan los pasos exactos aquí, ya que no es el objetivo principal de esta sección. Lo importante fue aprender a utilizar estas herramientas para corregir errores de integración y consolidar el historial de commits.
## 3.5 Reporte Detallado de Ramas y Commits

### Reporte Detallado del Manejo de Branches en Orden Cronológico

A continuación, se presenta una lista detallada de todas las ramas creadas en el proyecto, ordenadas cronológicamente según su fecha de creación. Para cada rama, se incluyen los detalles de los commits realizados, fechas, autores, merges y descripciones.

---
### 1. **`main`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-20**
- **Commit Inicial**:
  - **dd52aed** (2024-09-20): *"Initial commit: added README and .gitignore"* por **Jorge Barriga**

**Descripción**: Se estableció el repositorio inicial del proyecto, agregando los archivos base `README.md` y `.gitignore`.

---
### 2. **`feature/estructura-basica`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-20**
- **Commits**:
  - **6fff542** (2024-09-20): *"Se sube la estructura básica del Juego"* por **Renato200419**
- **Merge a `main`**:
  - **d89b1f1** (2024-09-20): *"Merge pull request #1 from Renato200419/feature/estructura-basica"* realizado por **Jorge Barriga**

**Descripción**: Se añadió la estructura fundamental del juego, estableciendo las bases para el desarrollo posterior.

---
### 3. **`feature/docker-setup`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-20**
- **Commits**:
  - **2d1ba9f** (2024-09-20): *"Subir Dockerfile"* por **Renato200419**
  - **cb0b4c7** (2024-09-20): *"Se configuró el puerto en main.py"* por **Renato200419**
- **Merge a `main`**:
  - **9d712f4** (2024-09-20): *"Merge pull request #2 from Renato200419/feature/docker-setup"* realizado por **Jorge Barriga**

**Descripción**: Se añadió el Dockerfile y se configuró el puerto en `main.py` para facilitar el despliegue de la aplicación en contenedores Docker.

---
### 4. **`feature/api`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-20**
- **Commits**:
  - **fd31007** (2024-09-20): *"Añadir class Jugador y la ruta para registrar jugadores"* por **Jorge Barriga**
  - **1470329** (2024-09-20): *"Añadir class Partida y la ruta para crear nuevas partidas"* por **Jorge Barriga**
  - **34885ba** (2024-09-20): *"Implementar la ruta para lanzar dados en una partida"* por **Jorge Barriga**
  - **9d92e9b** (2024-09-20): *"Reordenar y limpiar el código para mejorar legibilidad"* por **Jorge Barriga**
  - **15b2918** (2024-09-20): *"Implementar ruta para consultar estadísticas de partidas"* por **Jorge Barriga**
- **Merge a `main`**:
  - **8850d17** (2024-09-20): *"Merge pull request #3 from Renato200419/feature/api"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se desarrollaron las rutas principales de la API utilizando FastAPI, incluyendo funcionalidades para registrar jugadores, crear partidas, lanzar dados y consultar estadísticas.

---
### 5. **`feature/devsecops`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-20**
- **Commit**:
  - **6cc559f** (2024-09-20): *"Configuración de GitHub Workflows"* por **Jorge Barriga**
- **Merge a `main`**:
  - **d809ba9** (2024-09-20): *"Merge pull request #5 from Renato200419/feature/devsecops"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se configuraron los flujos de trabajo de GitHub Actions para integrar prácticas de DevSecOps en el proyecto, incluyendo integraciones continuas y análisis de seguridad.

---
### 6. **`fix/ci-pipeline`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-20**
- **Commits**:
  - **e799c19** (2024-09-20): *"Agregar CI pipeline para pruebas en GitHub Actions"* por **al-2100**
  - **ef939f7** (2024-09-20): *"Test en branch /fix/ci-pipeline"* por **Jorge Barriga**
  - **daa0434** (2024-09-20): *"Test en branch /fix/ci-pipeline"* por **Jorge Barriga**
  - **0672469** (2024-09-20): *"Agregar requirements.txt con dependencias del proyecto"* por **Jorge Barriga**
  - **2956a17** (2024-09-20): *"Retirar tests (temporalmente)"* por **Jorge Barriga**
  - **c6bd1f4** (2024-09-20): *"Retirar fix/ci-pipeline del pipeline CI"* por **Jorge Barriga**
- **Merge a `main`**:
  - **72fd1f1** (2024-09-20): *"Merge pull request #6 from Renato200419/fix/ci-pipeline"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se solucionaron problemas en el pipeline de integración continua, asegurando que las pruebas automáticas se ejecuten correctamente en GitHub Actions.

---
### 7. **`feature/interfaz-crear_partida`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-21**
- **Commit**:
  - **988a08b** (2024-09-21): *"Se agrega la función crear-partida"* por **Renato200419**
- **Merge a `feature/interfaz`**:
  - **61098d2** (2024-09-21): *"Merge pull request #9 from Renato200419/feature/interfaz-crear_partida"* realizado por **ISMA12345830**

**Descripción**: Se añadió la función para crear partidas en la interfaz de consola del juego.

---
### 8. **`feature/interfaz-mostrar_estadisticas`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-21**
- **Commit**:
  - **f26e094** (2024-09-21): *"Se agrega la función mostrar estadisticas"* por **ISMA12345830**
- **Merge a `feature/interfaz`**:
  - **cf0936d** (2024-09-21): *"Merge pull request #10 from Renato200419/feature/interfaz-mostrar_estadisticas"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se implementó la función para mostrar estadísticas de las partidas en la interfaz de consola.

---
### 9. **`feature/interfaz`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-21**
- **Commits**:
  - **c95e6e3** (2024-09-22): *"Se agregan más funciones para la interfaz consola: lanzar_dados y registrar_jugador"* por **Renato200419**
  - **48ea60b** (2024-09-22): *"Se agregó el menú principal"* por **ISMA12345830**
- **Merge a `main`**:
  - **9852026** (2024-09-22): *"Merge pull request #11 from Renato200419/feature/interfaz"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se consolidaron las funciones de creación de partida, registro de jugadores, lanzamiento de dados y visualización de estadísticas en la interfaz de consola.

---
### 10. **`feature/pruebas`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-22**
- **Commit**:
  - **6ab1738** (2024-09-22): *"Configurar pruebas básicas en test_app.py"* por **ISMA12345830**
- **Merge a `main`**:
  - **06cb580** (2024-09-22): *"Merge pull request #13 from Renato200419/feature/pruebas"* realizado por **Jorge Barriga**

**Descripción**: Se añadieron pruebas unitarias básicas para validar las funcionalidades principales de la aplicación.

---
### 11. **`feature/actualizar-ci`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-22**
- **Commits**:
  - **708f593** (2024-09-22): *"Modificar ci.yml para incluir CD de CI/CD"* por **ISMA12345830**
  - **4dc7276** (2024-09-22): *"Correcciones a ci.yml"* por **ISMA12345830**
  - **3d68ab0** (2024-09-22): *"Actualizar dependencias"* por **ISMA12345830**
  - **63a2071** (2024-09-22): *"Corregir pipeline"* por **ISMA12345830**
  - **a57ef67** (2024-09-22): *"Arreglar el error de indentación"* por **ISMA12345830**
  - **f29092b** (2024-09-22): *"Cambios a versiones"* por **ISMA12345830**
  - **a513ece** (2024-09-22): *"Cambiar a test con testclient"* por **ISMA12345830**
  - **08ed653** (2024-09-22): *"Establecer PYTHONPATH"* por **Jorge Barriga**
  - **c3660b9** (2024-09-22): *"Incluir la actualización de setuptools"* por **Jorge Barriga**
  - **69efee7** (2024-09-22): *"Eliminar Run API tests"* por **Jorge Barriga**
  - **d092361** (2024-09-22): *"Eliminar feature/actualizar-ci de 'on push'"* por **Jorge Barriga**
- **Merge a `main`**:
  - **4fb7d3f** (2024-09-22): *"Merge pull request #16 from Renato200419/feature/actualizar-ci"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se actualizó el pipeline de CI/CD para mejorar la integración y despliegue continuo, incluyendo ajustes en las versiones y dependencias.

---
### 12. **`prometheus-config`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-22**
- **Commit**:
  - **234ef9a** (2024-09-22): *"Crear prometheus.yml"* por **Renato200419**
- **Merge a `main`**:
  - **6199f8f** (2024-09-22): *"Merge pull request #14 from Renato200419/prometheus-config"* realizado por **ISMA12345830**

**Descripción**: Se añadió la configuración inicial de Prometheus para la recolección de métricas.

---
### 13. **`feature/docker-setup`**

- **Commits**:
  - **ed971b5** (2024-09-22): *"Actualizar docker-compose.yml para incluir Prometheus y Grafana"* por **Renato200419**
- **Merge a `main`**:
  - **7102deb** (2024-09-22): *"Merge pull request #15 from Renato200419/feature/docker-setup"* realizado por **ISMA12345830**

**Descripción**: Se actualizó el archivo `docker-compose.yml` para integrar los servicios de Prometheus y Grafana, permitiendo la monitorización y visualización de métricas.

---
### 14. **`feature/metrics`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-22**
- **Commits**:
  - **a93f901** (2024-09-22): *"Agregar prometheus_fastapi_instrumentator y prometheus_client"* por **Renato200419**
  - **95d2fdb** (2024-09-22): *"Modificar app.py para incluir métricas de tiradas y latencia"* por **Renato200419**
  - **064b019** (2024-09-22): *"Agregar dependencias a requirements.txt"* por **Renato200419**
  - **aa19308** (2024-09-22): *"Actualizar la forma en la que se instalan las dependencias"* por **Renato Steven Olivera Calderón**
- **Merge a `main`**:
  - **aa710ce** (2024-09-22): *"Merge pull request #19 from Renato200419/feature/metrics"* realizado por **Jorge Barriga**

**Descripción**: Se implementaron métricas personalizadas para la aplicación, incluyendo métricas de tiradas de dados y latencia de endpoints.

---
### 15. **`fix-missing-metrics`**

- **Creado por**: **Renato Steven Olivera Calderón**
- **Fecha de Creación**: **2024-09-22**
- **Commits**:
  - **440826f** (2024-09-22): *"Agregar prometheus_fastapi_instrumentator y prometheus_client"* por **Renato200419**
  - **63d03bc** (2024-09-22): *"Modificar app.py para incluir métricas de tiradas y latencia"* por **Renato200419**
  - **ca01784** (2024-09-22): *"Agregar dependencias a requirements.txt"* por **Renato200419**
  - **bd8a7eb** (2024-09-22): *"Actualizar la forma en la que se instalan las dependencias"* por **Renato Steven Olivera Calderón**
- **Merge a `main`**:
  - **33876ee** (2024-09-22): *"Merge pull request #20 from Renato200419/fix-missing-metrics"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se corrigieron problemas relacionados con la falta de ciertas métricas en la aplicación.

---
### 16. **`feature/configurar-prometheus-grafana`**

- **Creado por**: **Renato Steven Olivera Calderón**
- **Fecha de Creación**: **2024-09-22**
- **Commits**:
  - **9429051** (2024-09-22): *"Actualización del docker-compose para almacenar datos"* por **Renato Steven Olivera Calderón**
  - **08cbbad** (2024-09-22): *"Dashboard creado"* por **Renato Steven Olivera Calderón**
- **Merge a `main`**:
  - **ab3261f** (2024-09-22): *"Merge pull request #21 from Renato200419/feature/configurar-prometheus-grafana"* realizado por **Jorge Barriga**

**Descripción**: Se configuraron Prometheus y Grafana para almacenar datos de métricas de forma persistente y se creó un dashboard personalizado.

---
### 17. **`feature/documentation-docker`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-22**
- **Commits**:
  - **572a11f** (2024-09-22): *"Subir documentación Docker.md"* por **Renato200419**
  - **038f3ef** (2024-09-22): *"Subir carpeta que contiene la imagen(es) para la documentación"* por **Renato200419**
  - **e15afa1** (2024-09-22): *"Corrección de línea"* por **Renato200419**
- **Merge a `main`**:
  - **ce81973** (2024-09-22): *"Merge pull request #22 from Renato200419/feature/documentation-docker"* realizado por **Jorge Barriga**

**Descripción**: Se añadió documentación detallada sobre la configuración y uso de Docker en el proyecto.

---
### 18. **`feature/documentation-observability`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-23**
- **Commits**:
  - **2b86073** (2024-09-23): *"Se agrega el archivo Markdown que explica la Observabilidad en el proyecto"* por **Renato200419**
  - **b9233f6** (2024-09-23): *"Se agrega la carpeta Imágenes que se usará para la documentación"* por **Renato200419**
- **Merge a `main`**:
  - **fb5b4ea** (2024-09-23): *"Merge pull request #23 from Renato200419/feature/documentation-observability"* realizado por **Jorge Barriga**

**Descripción**: Se documentó la implementación de observabilidad en el proyecto, incluyendo el uso de Prometheus y Grafana.

---
### 19. **`feature/documentation-git-usage`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-23**
- **Commits**:
  - **6a996a7** (2024-09-23): *"Subir documentación del uso de Git y resolución de conflictos"* por **Renato200419**
  - **1f587c1** (2024-09-23): *"Subir carpeta de Imágenes que se usarán en la documentación"* por **Renato200419**
- **Merge a `main`**:
  - **66ef939** (2024-09-23): *"Merge pull request #24 from Renato200419/feature/documentation-git-usage"* realizado por **Jorge Barriga**

**Descripción**: Se añadió documentación sobre buenas prácticas en el uso de Git y cómo resolver conflictos durante el desarrollo colaborativo.

---
### 20. **`feature/documentation-devsecops`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-23**
- **Commits**:
  - **cad829d** (2024-09-23): *"Subir imágenes para documentación DevSecOps"* por **Jorge Barriga**
  - **97723af** (2024-09-23): *"Documentación DevSecOps"* por **Jorge Barriga**
- **Merge a `main`**:
  - **0d0e220** (2024-09-23): *"Merge pull request #25 from Renato200419/feature/documentation-devsecops"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se agregó documentación detallada sobre las prácticas de DevSecOps implementadas en el proyecto.

---
### 21. **`feature/documentation-api`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-23**
- **Commit**:
  - **e5507da** (2024-09-23): *"Documentación sobre la API"* por **Jorge Barriga**
- **Merge a `main`**:
  - **3eb50af** (2024-09-23): *"Merge pull request #26 from Renato200419/feature/documentation-api"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se documentó detalladamente la API del proyecto, incluyendo endpoints y ejemplos de uso.

---
### 22. **`feature/documentation-readme`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-23**
- **Commit**:
  - **bde777f** (2024-09-23): *"Actualización - README.md"* por **ISMA12345830**
- **Merge a `main`**:
  - **0887c00** (2024-09-23): *"Merge pull request #27 from Renato200419/feature/documentation-readme"* realizado por **ISMA12345830**

**Descripción**: Se actualizó el archivo `README.md` con información relevante sobre el proyecto.

---
### 23. **`feature/documentation-cherry-pick`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-23**
- **Commits**:
  - **5e6d680** (2024-09-23): *"Imágenes para la documentación de cherry-pick"* por **Jorge Barriga**
  - **8d8c575** (2024-09-23): *"Actualizar documentación: Incluir uso de cherry-pick"* por **Jorge Barriga**
- **Merge a `main`**:
  - **0e42352** (2024-09-23): *"Merge pull request #28 from Renato200419/feature/documentation-cherry-pick"* realizado por **ISMA12345830**

**Descripción**: Se añadió documentación sobre el uso de `git cherry-pick` para la gestión de commits específicos.

---
### 24. **`feature/documentation-client`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-23**
- **Commits**:
  - **1ab81e9** (2024-09-23): *"Agregando archivo.md"* por **ISMA12345830**
  - **7ec771b** (2024-09-23): *"Participación de los jugadores en las partidas"* por **ISMA12345830**
- **Merge a `main`**:
  - **5a53ddb** (2024-09-23): *"Merge pull request #29 from Renato200419/feature/documentation-client"* realizado por **Jorge Barriga**

**Descripción**: Se documentó la participación de los jugadores en las partidas y se añadieron detalles sobre el cliente del juego.

---
### 25. **`feature/BD-postgres-update-docker-compose`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-23**
- **Commit**:
  - **fe4500f** (2024-09-23): *"Subir actualización del docker-compose para que se conecte con el PostgreSQL"* por **Renato200419**
- **Merge a `main`**:
  - **3aabb44** (2024-09-23): *"Merge pull request #31 from Renato200419/feature/BD-postgres-update-docker-compose"* realizado por **Jorge Barriga**

**Descripción**: Se actualizó el archivo `docker-compose.yml` para integrar el servicio de PostgreSQL, permitiendo que la aplicación se conecte a la base de datos dentro del entorno Docker.

---
### 26. **`feature/metrics-update-contador-players`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-23**
- **Commit**:
  - **531c28a** (2024-09-23): *"Subir métrica de contador de jugadores registrados"* por **Renato200419**
- **Merge a `main`**:
  - **5521b1d** (2024-09-23): *"Merge pull request #33 from Renato200419/feature/metrics-update-contador-players"* realizado por **Jorge Barriga**
- **Reversión**:
  - **60d82f1** (2024-09-23): *"Revert 'Subir métrica de contador de jugadores registrados'"* por **Jorge Barriga**
- **Merge posterior**:
  - **0a1f028** (2024-09-23): *"Merge pull request #34 from Renato200419/revert-33-feature/metrics-update-contador-players"* realizado por **ISMA12345830**

**Descripción**: Se implementó una métrica para contar el número de jugadores registrados en la aplicación. Sin embargo, debido a conflictos o errores, se revirtió el commit y se realizó un merge para revertir los cambios.

---
### 27. **`feature/metrics-update-histogram`**

- **Creado por**: **al-2100**
- **Fecha de Creación**: **2024-09-23**
- **Commit**:
  - **b5b9033** (2024-09-23): *"Agregar métrica para jugadores con puntajes >=4"* por **al-2100**
- **Merge a `main`**:
  - **1daa3a2** (2024-09-23): *"Merge pull request #36 from Renato200419/feature/metrics-update-histogram"* realizado por **ISMA12345830**
- **Reversión**:
  - **3aa1236** (2024-09-25): *"Revert 'Agregar métrica para jugadores con puntajes >=4'"* por **Jorge Barriga**
- **Merge posterior**:
  - **af579a6** (2024-09-24): *"Merge pull request #38 from Renato200419/revert-36-feature/metrics-update-histogram"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se agregó una métrica para monitorear a los jugadores con puntajes mayores o iguales a 4. Debido a problemas, se revirtió el commit y se realizó un merge para revertir los cambios.

---
### 28. **`feature/metrics-update-jugadores_registrados`**

- **Creado por**: **Renato Steven Olivera Calderón**
- **Fecha de Creación**: **2024-09-24**
- **Commit**:
  - **34dca05** (2024-09-24): *"Subir métrica jugadores registrados"* por **Renato Steven Olivera Calderón**
- **Merge a `main`**:
  - **079874c** (2024-09-24): *"Merge pull request #39 from Renato200419/feature/metrics-update-jugadores_registrados"* realizado por **ISMA12345830**

**Descripción**: Se implementó una métrica para registrar el número total de jugadores en la aplicación.

---
### 29. **`feature/metrics-update-puntuaciones_altas`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-24**
- **Commit**:
  - **0ab67dd** (2024-09-24): *"Agregar métrica de puntuaciones altas para puntos mayores a 4"* por **Jorge Barriga**
- **Merge a `main`**:
  - **779b3c4** (2024-09-24): *"Merge pull request #40 from Renato200419/feature/metrics-update-puntuaciones_altas"* realizado por **ISMA12345830**

**Descripción**: Se añadió una métrica para rastrear las puntuaciones altas, específicamente para los puntos mayores a 4.

---
### 30. **`feature/metrics-update-cantidad_partidas`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-24**
- **Commit**:
  - **9142746** (2024-09-24): *"Agregar las métricas de la cantidad de partidas creadas"* por **ISMA12345830**
- **Merge a `main`**:
  - **bad5e3a** (2024-09-24): *"Merge pull request #42 from Renato200419/feature/metrics-update-cantidad_partidas"* realizado por **Jorge Barriga**

**Descripción**: Se implementó una métrica para contar el número de partidas creadas en la aplicación.

---
### 31. **`feature/metrics-update`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-24**
- **Merge a `main`**:
  - **558fed6** (2024-09-24): *"Merge pull request #43 from Renato200419/feature/metrics-update"* realizado por **ISMA12345830**

**Descripción**: Esta rama consolidó las actualizaciones de métricas realizadas en las ramas anteriores, integrando todas las nuevas métricas implementadas.

---
### 32. **`feature/refactor-structure`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-27**
- **Commits**:
  - **a4568b6** (2024-09-27): *"Reorganiza la estructura del proyecto y renombra archivos"* por **Jorge Barriga**
  - **e0468a4** (2024-09-27): *"Modificar Dockerfile para la nueva estructura"* por **Jorge Barriga**
  - **58160b7**, **535bcee**, **520955a** (2024-09-27): *"Actualizar PYTHONPATH en ci.yml para incluir el directorio raíz y app/"* por **Jorge Barriga**
- **Merge a `main`**:
  - **b8cc60b** (2024-09-27): *"Merge pull request #44 from Renato200419/feature/refactor-structure"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se reorganizó la estructura del proyecto para mejorar la mantenibilidad y escalabilidad, incluyendo cambios en la estructura de carpetas y archivos, y ajustes en el Dockerfile y el pipeline de CI.

---
### 33. **`feature/database-integration`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-27**
- **Commits**:
  - **e4b5790** (2024-09-27): *"Añadir modelos de Jugador y Partida con Peewee"* por **Renato200419**
  - **8e726ab** (2024-09-27): *"Configurar conexión a PostgreSQL e inicializar tablas"* por **Renato200419**
  - **4287cb5** (2024-09-27): *"Agregar funciones CRUD para Jugador y Partida"* por **Renato200419**
- **Merge a `main`**:
  - **25bb6b6** (2024-09-27): *"Merge pull request #45 from Renato200419/feature/database-integration"* realizado por **Jorge Barriga**

**Descripción**: Se integró la base de datos PostgreSQL al proyecto utilizando el ORM Peewee, permitiendo operaciones CRUD sobre los modelos Jugador y Partida.

---
### 34. **`feature/metrics-and-endpoints`**

- **Creado por**: **Jorge Barriga**
- **Fecha de Creación**: **2024-09-27**
- **Commits**:
  - **14d3d1b** (2024-09-27): *"Implementar rutas para gestionar jugadores y partidas en routes.py"* por **Jorge Barriga**
  - **4cfc3bf** (2024-09-27): *"Modificar main.py para exponer las rutas y métricas"* por **Jorge Barriga**
  - **d106d8a** (2024-09-27): *"Actualizar dependencias"* por **Jorge Barriga**
  - **fe76c33** (2024-09-27): *"Añadir dependencias"* por **Jorge Barriga**
  - **e0b4c79** (2024-09-27): *"Agregar servicio de PostgreSQL en GitHub Actions"* por **Jorge Barriga**
- **Commits adicionales**:
  - **dcd5c47** (2024-09-28): *"Se incluye el servicio de PostgreSQL"* por **Renato200419**
  - **dab3a8c** (2024-09-28): *"Se incluye un paso de espera adicional antes de ejecutar la aplicación"* por **Renato200419**
  - **Ajustes en el pipeline y configuraciones adicionales** por **Jorge Barriga** y **Renato200419**
- **Merge a `main`**:
  - **51949a3** (2024-09-29): *"Merge pull request #46 from Renato200419/feature/metrics-and-endpoints"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se añadieron nuevas rutas en la API para gestionar jugadores y partidas utilizando la base de datos, y se expusieron métricas adicionales. Se ajustó el pipeline de CI/CD para incluir PostgreSQL en las pruebas automatizadas.

---
### 35. **`feature/docker-compose-update`**

- **Creado por**: **Renato Steven Olivera Calderón**
- **Fecha de Creación**: **2024-09-29**
- **Commit**:
  - **5dad30a** (2024-09-29): *"Se actualiza el docker-compose con los volúmenes persistentes de Prometheus"* por **Renato Steven Olivera Calderón**
- **Merge a `main`**:
  - **9dde777** (2024-09-29): *"Merge pull request #47 from Renato200419/feature/docker-compose-update"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se actualizó el `docker-compose.yml` para incluir volúmenes persistentes para Prometheus, permitiendo que los datos de métricas se mantengan entre reinicios.

---
### 36. **`feature/mejorar_consola`**

- **Creado por**: **ISMA12345830**
- **Fecha de Creación**: **2024-09-30**
- **Commits**:
  - **e47caab** (2024-09-30): *"Mejoramiento del funcionamiento del game_console.py"* por **ISMA12345830**
  - **4af76c8** (2024-09-30): *"Corrección de espacios del funcionamiento del game_console.py"* por **ISMA12345830**
  - **24f36dd** (2024-09-30): *"Implementación de una funcionalidad del routes.py"* por **ISMA12345830**
  - **7e38d2c** (2024-09-30): *"Implementación de la funcionalidad en el crud.py"* por **ISMA12345830**
  - **73f7758** (2024-09-30): *"Corrección del crud.py"* por **ISMA12345830**
  - **2cc41a5** (2024-09-30): *"Cambiar código esperado de 201 a 200"* por **Jorge Barriga**
- **Merge a `main`**:
  - **5030ba9** (2024-09-30): *"Merge pull request #48 from Renato200419/feature/mejorar_consola"* realizado por **Renato Steven Olivera Calderón**

**Descripción**: Se mejoró el funcionamiento de la consola del juego, corrigiendo errores y optimizando la interacción con el usuario.

---
### 37. **`feature/update_console`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-10-01**
- **Commits**:
  - **39c1564** (2024-10-01): *"Evitar creación automática de jugadores no registrados al crear partida"* por **Renato200419**
  - **01efef5** (2024-10-01): *"Agrega atributo para contar victorias del jugador e importa IntegerField"* por **Renato200419**
  - **b7824d6** (2024-10-01): *"Se crea el endpoint mostrar_ranking"* por **Renato200419**
  - **fa69565** (2024-10-01): *"Se modifica routes.py para calcular y devolver el cambio de ranking"* por **Renato200419**
  - **f1c8b1f** (2024-10-01): *"Modifica la función lanzar_dados para reflejar el cambio de posición"* por **Renato200419**
  - **e943b3a** (2024-10-01): *"Se elimina el comentario del menú"* por **Renato200419**
  - **588c653** (2024-10-01): *"Mejorar lógica de creación de partida y validación de puntajes"* por **Renato200419**
  - **b00f838** (2024-10-01): *"Agregar atributo de partidas jugadas al modelo Jugador"* por **Renato200419**
  - **7ff3161** (2024-10-01): *"Incrementar el contador de partidas jugadas al finalizar cada partida"* por **Renato200419**
  - **7a3801d** (2024-10-01): *"Modificación del título de ranking así como la función"* por **Renato200419**
- **Merge a `main`**:
  - **bac1385** (2024-10-01): *"Merge pull request #49 from Renato200419/feature/update_console"* realizado por **Jorge Barriga**
- **Etiqueta**:
  - **v1.1.0**

**Descripción**: Se añadieron nuevas funcionalidades a la consola del juego, incluyendo la gestión de rankings y estadísticas de jugadores. Se lanzó la versión **v1.1.0** del proyecto.

---
### 38. **`feature/documentacion-pc1`**

- **Creado por**: **Renato200419**
- **Fecha de Creación**: **2024-09-27**
- **Commits**:
  - **f4c1296** (2024-09-27): *"Agregar índice general en documentacion-pc1.md"* por **Renato Steven Olivera Calderón**
  - **0b5eba6** (2024-09-27): *"Se agrega el manejo de ramas en el proyecto del punto 1-10"* por **Renato200419**
  - **156731a** (2024-09-27): *"Manejo de ramas del punto 11 al 19"* por **Jorge Barriga**
  - **e917f8f** (2024-09-27): *"Eliminación de antiguos Markdown"* por **Renato200419**
  - **7ea165a** (2024-09-29): *"Reestructuración del índice de la documentación"* por **Renato Steven Olivera Calderón**
  - **60f0d83** (2024-09-29): *"Se sube avance de la documentación de Docker y Docker-Compose incluyendo el servicio de PostgreSQL"* por **Renato200419**
  - **b471c61** (2024-09-29): *"Subir imagen del gráfico de red de todas las ramas creadas"* por **Renato200419**
  - **712c845** (2024-09-29): *"Subir avance de la documentación de la gestión del proyecto con Git"* por **Renato200419**
  - **1bc3de7** (2024-09-30): *"Añadir imágenes para documentación"* por **Jorge Barriga**
  - **2c5f417** (2024-09-30): *"Actualización y mejora del documento"* por **Jorge Barriga**

**Descripción**: Se amplió y mejoró la documentación del proyecto, detallando el manejo de ramas y merges en el repositorio, y agregando información sobre Docker, Docker-Compose y PostgreSQL (Falta el último commit y el commit de merge pues no es posible saberlo).

### Gráfico de Red luego de la creación de todas las ramas
![Descripción de la imagen](Imagenes-git/GN.jpg)

---

# 4. DevOps y DevSecOps

## 4.1 Propósito

El propósito de esta sección es explicar cómo se ha implementado DevOps y DevSecOps en el proyecto, integrando prácticas de desarrollo, operaciones y seguridad para garantizar que el ciclo de vida del software sea seguro, eficiente y automatizado. Se detalla cómo la seguridad y la automatización se integran en cada fase del pipeline de CI/CD, desde la instalación de dependencias hasta la auditoría de vulnerabilidades, la ejecución de pruebas y el despliegue en entornos contenerizados.
## 4.2 Pipeline de CI/CD

Se utilizó **GitHub Actions** para automatizar el pipeline de CI/CD del proyecto, permitiendo la integración continua (CI) y la entrega continua (CD). Esto se configuró en el archivo `ci.yml`, que define las diferentes etapas para cada cambio en el código. El pipeline se activa automáticamente con cada push o pull request en la rama `main`, realizando las siguientes tareas:

### Descripción de cada paso del Pipeline CI/CD

1. **Configuración de Servicios (Base de Datos)**:
   - **Servicios**: El pipeline inicializa un servicio de PostgreSQL que se ejecuta en un contenedor. Esto asegura que la base de datos esté disponible durante la ejecución de pruebas.
   - **Verificación de Salud**: Se configuran comandos de `health-check` para asegurar que la base de datos esté lista antes de ejecutar pruebas dependientes de ella.

   ```yaml
   services:
     db:
       image: postgres:13
       env:
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: secret
         POSTGRES_DB: dadosdb
       ports:
         - 5432:5432
       options: >-
         --health-cmd "pg_isready -U admin -d dadosdb" 
         --health-interval 10s 
         --health-timeout 5s 
         --health-retries 10
   ```

2. **Checkout del Código**:
   - **Acción**: Se descarga el código desde el repositorio de GitHub. Esto asegura que la última versión del código en `main` esté disponible para las siguientes etapas.

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v2
   ```

3. **Configuración del Entorno Python**:
   - **Acción**: Configura el entorno de Python en la versión 3.8. Esto es necesario para que las dependencias se instalen correctamente y las pruebas se ejecuten en el entorno adecuado.

   ```yaml
   - name: Set up Python
     uses: actions/setup-python@v3
     with:
       python-version: '3.8'
   ```

4. **Instalación de Dependencias**:
   - **Acción**: Se instalan todas las dependencias especificadas en `requirements.txt`. Esto asegura que todas las librerías necesarias para la ejecución de la aplicación estén disponibles en el entorno.

   ```yaml
   - name: Install dependencies
     run: |
       python -m pip install --upgrade pip
       pip install --upgrade setuptools
       pip install -r requirements.txt
   ```

5. **Esperar a que la Base de Datos esté lista**:
   - **Acción**: Verifica que PostgreSQL esté listo antes de ejecutar cualquier prueba que dependa de la base de datos. Esto evita errores en la conexión a la base de datos durante la ejecución de pruebas.

   ```yaml
   - name: Wait for PostgreSQL to be ready
     run: |
       echo "Waiting for PostgreSQL to be ready..."
       until pg_isready -h localhost -p 5432 -U admin -d dadosdb; do
         sleep 5
       done
       echo "PostgreSQL is ready!"
   ```

6. **Ejecución de Pruebas**:
   - **Acción**: Ejecuta las pruebas definidas en el directorio `tests/` utilizando `pytest`. Se establece la variable de entorno `DATABASE_URL` para conectar con la base de datos en el contenedor.

   ```yaml
   - name: Run tests
     env:
       DATABASE_URL: postgresql://admin:secret@localhost:5432/dadosdb
       PYTHONPATH: .
     run: |
       pytest tests/
   ```

7. **Instalación y Ejecución de Auditorías de Seguridad**:
   - **Acción**: Se instala `pip-audit` y se ejecuta para detectar vulnerabilidades en las dependencias del proyecto.

   ```yaml
   - name: Install pip-audit
     run: pip install pip-audit

   - name: Audit dependencies
     run: pip-audit
   ```

8. **Construcción de Imagen Docker**:
   - **Acción**: Construye una imagen Docker para la aplicación usando el `Dockerfile` definido en el proyecto. Esta imagen contiene todo el entorno necesario para ejecutar la aplicación de forma aislada.

   ```yaml
   - name: Build Docker image
     run: docker build -t juego-dados-competitivo .
   ```

9. **Creación de Red Docker**:
   - **Acción**: Se crea una red Docker para conectar la base de datos y la aplicación en un entorno aislado.

   ```yaml
   - name: Create Docker network
     run: docker network create juego-dados-network
   ```

10. **Despliegue en Contenedores**:
    - **Acción**: Despliega la aplicación en un contenedor Docker y la conecta a la red creada previamente.

    ```yaml
    - name: Run Docker container
      run: |
        docker run -d --network juego-dados-network --name juego-dados -p 8000:8000 juego-dados-competitivo
    ```

11. **Verificación del Estado de los Contenedores**:
    - **Acción**: Muestra el estado de todos los contenedores para verificar que todo esté funcionando correctamente.

    ```yaml
    - name: Verify container status
      run: docker ps -a
    ```

12. **Detención y Eliminación de Contenedores y Red**:
    - **Acción**: Detiene y elimina los contenedores y la red creados para mantener el entorno limpio.

    ```yaml
    - name: Stop and remove containers and network
      run: |
        docker stop juego-dados
        docker rm juego-dados
        docker network rm juego-dados-network
    ```

## 4.3 Configuración de Análisis de Seguridad y Pruebas Automatizadas

### 4.3.1 Herramientas de Auditoría

Para garantizar la seguridad del código y la estabilidad del proyecto, se integraron las siguientes herramientas:

- **pip-audit**: Audita las dependencias del proyecto para detectar vulnerabilidades conocidas en paquetes de Python. Se ejecuta automáticamente en cada cambio en el código y alerta al equipo en caso de encontrar alguna vulnerabilidad.

- **pytest**: Se utilizó para definir pruebas automáticas que verifican la correcta funcionalidad de la API.

Ejemplo de cómo pip-audit detecta vulnerabilidades y falla el pipeline:
![Descripción de la imagen](Imagenes/pip-audit.png)
Medidas tomadas:
![Medidas tomadas](Imagenes/medidas.png)
### 4.3.2 Ejecución de Auditorías de Seguridad Manuales

Si se desean realizar auditorías de seguridad de forma manual, se pueden seguir los siguientes pasos:

1. Asegurarse de tener **pip-audit** instalado:
   
   ```bash
   pip install pip-audit
   ```

2. Ejecutar la auditoría de seguridad con el siguiente comando:

   ```bash
   pip-audit
   ```

Esto generará un informe detallando cualquier vulnerabilidad detectada en las dependencias del proyecto.

### 4.3.3 Reflexión sobre el Impacto de DevOps en el Proyecto

La implementación de DevOps y DevSecOps en el proyecto no solo facilitó la integración continua y la entrega continua (CI/CD), sino que también permitió mantener altos estándares de seguridad y calidad. Al automatizar pruebas, auditorías y despliegues, se logró detectar problemas de manera proactiva y asegurar la estabilidad del software en cada entrega.

Otro ejemplo de como el pipeline CI/CD ayuda en el proceso de las Pull Request:
![ci/cd-pr](Imagenes/PR44.png)
Nos asegura solo aceptar cambios que mantienen los estándares de seguridad y calidad.

---

### 4.4 Reflexión sobre el Flujo de Trabajo DevOps

El enfoque DevOps utilizado en este proyecto combina desarrollo, seguridad y operaciones de manera efectiva. Algunas ventajas y reflexiones sobre el impacto de estas prácticas son:

- **Automatización y Eficiencia**: El uso de GitHub Actions para la integración continua permitió la automatización de tareas repetitivas, como la ejecución de pruebas y auditorías de seguridad, reduciendo el tiempo necesario para asegurar la calidad del software.
- **Entrega Continua**: La contenerización de la aplicación y su despliegue automatizado en contenedores Docker aseguraron que cualquier cambio realizado pudiera ser probado y desplegado fácilmente en entornos controlados.
- **Integración de Seguridad (DevSecOps)**: La integración de pip-audit como parte del pipeline CI/CD permitió detectar vulnerabilidades en las dependencias de manera automática, mejorando la postura de seguridad del proyecto.

En general, la implementación de DevOps y DevSecOps ha sido fundamental para asegurar un flujo de desarrollo continuo, estable y seguro, manteniendo la calidad del proyecto en todas sus etapas.

---

# 5. Cambios Clave Impulsados por la Inclusión de PostgreSQL

## 5.1 Reestructuración del Proyecto

### Contexto de la Reestructuración

Inicialmente, la aplicación estaba contenida en dos archivos principales:

- **`app.py`**: Incluía toda la lógica de la API, como el registro de jugadores, la creación de partidas y el lanzamiento de dados. Además, almacenaba todos los datos en listas dentro del mismo archivo, lo que limitaba la persistencia y mantenibilidad del proyecto.
- **`main.py`**: Funcionaba como la **consola del juego**, permitiendo a los usuarios interactuar con la API a través de un menú de opciones.

Este enfoque limitaba la escalabilidad y mantenibilidad del proyecto. La práctica calificada del lunes 23 impulsó la integración de una base de datos **PostgreSQL**, lo cual requería cambios sustanciales en la arquitectura del proyecto. A partir de esto, se realizó una reestructuración completa del código.

### Cambios Realizados en la Estructura de Archivos

Para mejorar la modularidad y mantenibilidad del proyecto, la aplicación se reestructuró en múltiples archivos dentro de un directorio `app/`. A continuación se presenta una comparación detallada de cómo era la estructura del proyecto antes y después de los cambios:

#### Estructura Anterior:
- **`app.py`**:  
  Contenía todas las rutas de la API y la lógica del juego, como se muestra en el ejemplo proporcionado.
  
- **`main.py`**:  
  Permitía ejecutar la consola del juego y realizar operaciones como registrar jugadores y lanzar dados a través de un menú interactivo.

#### Nueva Estructura:
- **`app/`**:
  - **`config.py`**: Configuración de la base de datos PostgreSQL.
  - **`crud.py`**: Operaciones CRUD para interactuar con la base de datos, como la creación de jugadores y partidas.
  - **`database.py`**: Inicializa la base de datos y las tablas necesarias.
  - **`main.py`**: Punto de entrada principal de la aplicación, utilizando `FastAPI`.
  - **`models.py`**: Definición de los modelos `Jugador` y `Partida` utilizando `Peewee`.
  - **`routes.py`**: Define las rutas de la API, separando claramente la lógica de registro, creación de partidas, lanzamiento de dados y obtención de estadísticas.

- **`game_console.py`**:  
  El antiguo `main.py` se movió a `game_console.py`, ya que ahora actúa como la consola del juego que permite a los jugadores interactuar con la API de forma local.

- **`docker-compose.yml`**:  
  El archivo `docker-compose.yml` se actualizó para incluir tanto la base de datos `PostgreSQL` como el servicio de la API.

### Impacto de la Reestructuración

Los cambios en la estructura del proyecto resultaron en mejoras significativas:

- **Modularización**: Cada archivo `.py` tiene una responsabilidad específica, facilitando la comprensión y colaboración en el desarrollo.
- **Persistencia de Datos**: La base de datos PostgreSQL almacena de manera persistente la información de jugadores y partidas.
- **Mejora en la Mantenibilidad**: La nueva estructura facilita el desarrollo de nuevas funcionalidades y la resolución de problemas.

### Comparación Visual de las Estructuras de Archivos

**Antes**:

```
project/
├── app.py
└── main.py
```

**Después**:

```
project/
├── app/
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── game_console.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 5.2 Implementación de la Persistencia de Datos con PostgreSQL

### Contexto de la Migración

Antes de la integración de PostgreSQL, los datos del juego se almacenaban en listas dentro del archivo `app.py` (`jugadores_registrados` y `partidas`). Esto significaba que cada vez que el servidor se reiniciaba, se perdía toda la información, lo cual no era viable para un entorno de producción.

### Cambios en la Lógica de la API

Con la inclusión de PostgreSQL, se crearon nuevos modelos de datos en `models.py` para representar las tablas `Jugador` y `Partida`. Las operaciones CRUD se trasladaron a `crud.py` para gestionar la interacción con la base de datos. Además, se definió una conexión centralizada en `config.py`.

### Implementación y Configuración

La conexión a PostgreSQL se configuró en `config.py` y la base de datos se inicializó en `database.py`:

**Fragmento de `config.py`:**

```python
from peewee import PostgresqlDatabase

# Configuración de la conexión a la base de datos PostgreSQL
db = PostgresqlDatabase(
    'dadosdb',
    user='admin',
    password='secret',
    host='db',
    port=5432
)
```

**Fragmento de `database.py`:**

```python
from .config import db
from .models import Jugador, Partida, JugadoresPartidas

# Inicialización de la base de datos y creación de tablas
def initialize_db():
    db.connect()
    db.create_tables([Jugador, Partida, JugadoresPartidas])
```

### Resultados Obtenidos

Con la implementación de la base de datos:

- **Persistencia de Datos**: Los datos se mantienen entre sesiones y reinicios de la aplicación.
- **Consultas Eficientes**: Se pueden ejecutar consultas complejas sobre los datos almacenados de manera más eficiente usando SQL a través de `Peewee`.
- **Facilidad para Reportes**: Permite generar estadísticas y reportes a partir de los datos almacenados de los jugadores y partidas.

## 5.3 Monitorización de Tiradas y Puntuaciones con Prometheus

### Contexto de la Monitorización

La práctica calificada también incluyó la implementación de monitorización con **Prometheus** para capturar y analizar métricas clave del proyecto. Inicialmente, solo se monitoreaban el **número total de tiradas** y la **latencia de las solicitudes**. Se añadieron nuevas métricas para reflejar mejor el comportamiento de la API.

### Nuevas Métricas Implementadas

1. **Contador de Jugadores (`jugadores_counter`)**:  
   Registra cuántos jugadores han sido añadidos a la base de datos.
   
2. **Contador de Partidas (`partidas_counter`)**:  
   Monitorea el número total de partidas creadas.
   
3. **Histograma de Puntuaciones (`puntajes_histogram`)**:  
   Muestra la distribución de las puntuaciones alcanzadas por los jugadores durante el juego.

### Resultados de la Monitorización

Con la integración de estas métricas adicionales:

- **Mayor Observabilidad**: Los gráficos en Grafana muestran en tiempo real la actividad de la API y el comportamiento de los jugadores.
- **Monitoreo en Tiempo Real**: Se pueden observar patrones y tendencias en las puntuaciones y actividad del juego.

### Fragmento de Código para Métricas

**Definición de Métricas en `routes.py`:**

```python
from prometheus_client import Counter, Histogram

# Métricas de Prometheus
jugadores_counter = Counter("jugadores_registrados_totales", "Total de jugadores registrados")
partidas_counter = Counter("partidas_creadas_totales", "Total de partidas creadas")
tiradas_counter = Counter("tiradas_totales", "Total de tiradas realizadas")
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")
puntajes_histogram = Histogram("puntajes_altos", "Distribución de puntuaciones altas", buckets=[10, 20, 30, 40, 50, 60])
```

## 5.4 Cambios en las Pruebas Automáticas y su Impacto

### Contexto de las Pruebas Antes de la Inclusión de PostgreSQL

Antes de integrar PostgreSQL y reestructurar la aplicación, se tenía un archivo de pruebas `tests/test_app.py` que funcionaba correctamente para verificar el comportamiento de la API. Este archivo permitía probar funcionalidades como:

- **`test_root()`**: Verificaba que el endpoint principal (`/`) respondiera correctamente con el mensaje de bienvenida.
- **`test_crear_partida()`**: Probaba la creación de una nueva partida utilizando datos simulados.
- **`test_lanzar_dados()`**: Comprobaba el correcto funcionamiento del lanzamiento de dados en una partida.

El archivo `test_app.py` funcionaba bien en el contexto anterior porque la API utilizaba listas locales para almacenar los datos (`jugadores_registrados` y `partidas`). No había necesidad de realizar conexiones con una base de datos externa, lo que hacía que las pruebas fueran más sencillas y rápidas de ejecutar.

**Fragmento del Archivo de Pruebas Anterior (`tests/test_app.py`):**

```python
from fastapi.testclient import TestClient
from app import app  # Importación directa del app original

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Juego de Dados"}

def test_crear_partida():
    jugadores = [{"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}]
    response = client.post("/partidas/", json=jugadores)
    assert response.status_code == 200
    assert "Partida" in response.json()["mensaje"]

def test_lanzar_dados():
    jugadores = [{"nombre": "Jugador 1"}, {"nombre": "Jugador 2"}]
    response = client.post("/partidas/", json=jugadores)
    partida_id = response.json()['partida']['id']

    response = client.post(f"/partidas/{partida_id}/lanzar")
    assert response.status_code == 200
    assert "Dados lanzados" in response.json().get('mensaje')
```

### Problemas al Integrar PostgreSQL

Cuando se migró a PostgreSQL, el archivo de pruebas `tests/test_app.py` dejó de funcionar debido a las siguientes razones:

1. **Dependencia de la Base de Datos**:
   - El sistema anterior no requería una base de datos, mientras que la nueva arquitectura depende de PostgreSQL para almacenar y consultar datos. Las pruebas automáticas deben conectarse a una base de datos real o simulada para funcionar correctamente.

2. **Configuración de Conexión**:
   - Al ejecutar `client.post` para registrar jugadores o crear partidas, las pruebas ahora fallan si no hay una base de datos disponible con la configuración adecuada. Anteriormente, las pruebas no dependían de la configuración de `DATABASE_URL` ni de la inicialización de tablas.

3. **Inicialización de Datos**:
   - Las pruebas ahora deben incluir configuraciones adicionales para inicializar y limpiar datos de la base de datos antes y después de cada prueba. Esto agrega una capa adicional de complejidad que no estaba presente antes.

### Cambios en el Archivo de Pruebas

Debido a los problemas mencionados, el archivo de pruebas `tests/test_app.py` se modificó para dejar de probar ciertas funcionalidades que dependen directamente de la base de datos, mientras se trabaja en adaptar las pruebas para el nuevo contexto:

**Fragmento del Archivo de Pruebas Actual (`tests/test_app.py`):**

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al Juego de Dados"}

# Pruebas eliminadas por el momento
```

Como se observa, las pruebas para `test_crear_partida()` y `test_lanzar_dados()` fueron eliminadas debido a que no es posible ejecutarlas sin una base de datos operativa. Actualmente, solo se mantiene la prueba `test_root()` para verificar que la API esté funcionando correctamente.

### Pasos a Seguir para Rehabilitar las Pruebas

Para adaptar `tests/test_app.py` al nuevo entorno con PostgreSQL, se deben realizar los siguientes cambios:

1. **Configuración de la Base de Datos para Pruebas**:
   - Crear una base de datos específica para pruebas que se inicialice y se destruya cada vez que se ejecuten las pruebas. Esto se puede hacer utilizando el contexto `pytest` y configuraciones de conexión temporales.

2. **Mocking de la Base de Datos**:
   - Utilizar herramientas como `pytest-mock` para simular las operaciones de la base de datos y evitar la necesidad de una base de datos real durante las pruebas.
## 5.5 Reflexión sobre los Cambios en el Proyecto

La integración de PostgreSQL transformó profundamente la estructura del proyecto, permitiendo una persistencia de datos confiable y separando claramente la lógica de la API en módulos específicos. Este cambio mejoró la organización y facilitó el desarrollo colaborativo, pero también presentó nuevos desafíos en la gestión de pruebas automáticas y la configuración de entornos.

La inclusión de métricas avanzadas con Prometheus y la visualización en Grafana aumentaron la observabilidad, proporcionando una visión más clara del rendimiento y uso de la API en tiempo real. Sin embargo, estos avances implicaron una reestructuración completa del código, desde un enfoque monolítico basado en memoria hacia un sistema más complejo con múltiples servicios interdependientes.

Aunque las pruebas automáticas quedaron temporalmente limitadas debido a la dependencia de la base de datos, el siguiente paso será restablecerlas y optimizarlas para que reflejen esta nueva arquitectura. En resumen, los cambios realizados fortalecen la solidez y escalabilidad del proyecto, dejando claro que, a pesar de los desafíos, la evolución hacia una estructura modular y persistente fue un paso esencial para llevar la aplicación a un entorno de producción más maduro y robusto.


# 6. Retrospectiva del Proyecto y Dificultades Encontradas

A lo largo del desarrollo del proyecto, el equipo enfrentó varios retos técnicos y de coordinación. A continuación se detallan las dificultades más relevantes, junto con una reflexión final sobre el proceso y el aprendizaje obtenido.

## 6.1 Dificultades Técnicas

### a. Migración a PostgreSQL
La migración desde un sistema basado en memoria hacia una base de datos relacional como PostgreSQL representó un reto significativo. Esto implicó reescribir y adaptar el código para utilizar nuevas funciones CRUD y asegurar que la estructura de la base de datos reflejara correctamente las relaciones entre las entidades del juego. Este cambio, aunque complejo, mejoró la persistencia de datos y sentó las bases para futuras extensiones del proyecto.

### b. Problemas con Pruebas Automáticas
La integración de PostgreSQL dificultó la ejecución de pruebas automatizadas, que anteriormente se basaban en datos en memoria. El equipo aún trabaja en adaptar estas pruebas al nuevo entorno para que puedan manejar conexiones de base de datos, inicialización y limpieza de datos. Resolver este problema será un paso esencial para validar completamente la funcionalidad de la API en el contexto actual.

### c. Configuración de Contenedores y CI/CD
La integración de Docker y Docker Compose trajo consigo problemas de configuración y conectividad entre servicios, especialmente al añadir Prometheus y Grafana. Además, la configuración del pipeline de CI/CD en GitHub Actions resultó en múltiples errores debido a dependencias y a la conexión con la base de datos. Finalmente, se logró estabilizar el pipeline y automatizar la verificación y despliegue del proyecto.

## 6.2 Retos en el Trabajo en Equipo

### a. Coordinación a Través de WhatsApp y Discord
El equipo se comunicaba principalmente a través de WhatsApp y se organizaba con reuniones en Discord para discutir el progreso y coordinar tareas en paralelo. A pesar de estos esfuerzos, surgieron errores al momento de trabajar en ramas y Pull Requests, debido a la falta de experiencia en el manejo adecuado de git y/o GitHub. Por ejemplo, hubo ocasiones en las que alguien no cambiaba bien de rama o hacía mal una PR.

### b. Problemas con PRs y Fusión de Ramas
En algunas ocasiones, se aceptaron PRs de forma apresurada sin una revisión exhaustiva, debido a la confianza en que el código estaba correcto. Esto generó situaciones en las que código que debía fusionarse con otra rama antes de llegar a `main` terminó fusionado directamente en `main`, causando desorden en el historial del proyecto y la necesidad de revertir cambios.

### c. Adaptación al GitHub Flow
Los errores cometidos al gestionar ramas y PRs se debieron principalmente a que el equipo no estaba acostumbrado a utilizar el flujo de trabajo GitHub Flow. Esta falta de familiaridad inicial llevó a malas prácticas, como fusiones prematuras o incorrectas. Sin embargo, estos contratiempos sirvieron para reforzar nuestra comprensión del proceso, mejorar la coordinación y aprender a seguir de manera más rigurosa el flujo de trabajo, lo cual resultó en una mejor integración y organización del proyecto hacia el final.

## 6.4 Reflexión Final

A pesar de los desafíos técnicos, las dificultades en la coordinación del equipo y los errores en la gestión de ramas, el proyecto logró evolucionar hacia una aplicación más sólida y escalable. La integración de PostgreSQL, la mejora en la observabilidad con Prometheus y Grafana, y el esfuerzo en la documentación detallada, sentaron las bases para un proyecto bien estructurado.

El equipo demostró resiliencia y capacidad para adaptarse, abordando problemas complejos y aprendiendo de cada error. Aunque algunas dificultades se originaron por la falta de experiencia con el GitHub Flow, cada error fue una oportunidad para reforzar estas áreas y seguir mejorando la colaboración en equipo. La experiencia adquirida en este proyecto fortalecerá futuros desarrollos, consolidando un enfoque más maduro y profesional para el desarrollo de software en entornos colaborativos.
