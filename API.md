# API REST - Juego de Dados Competitivo

## Propósito
Esta API permite gestionar partidas y jugadores en un juego de dados competitivo. Se pueden registrar jugadores, crear partidas, lanzar dados, y obtener estadísticas de las partidas.
## Endpoints de la API

### 1. **Registrar Jugador**
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

### 2. **Crear Partida**
- **URL**: `/partidas/`
- **Método**: `POST`
- **Descripción**: Crea una nueva partida con al menos dos jugadores.
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
    "partida": {
      "id": 1,
      "jugadores": [
        {"nombre": "jugador1"},
        {"nombre": "jugador2"}
      ],
      "puntajes": {
        "jugador1": 0,
        "jugador2": 0
      }
    }
  }
  ```
- **Errores**:
  - `400`: Se requieren al menos 2 jugadores.
  ```json
  {
    "detail": "Se requieren al menos 2 jugadores"
  }
  ```

### 3. **Lanzar Dados**
- **URL**: `/partidas/{partida_id}/lanzar`
- **Método**: `POST`
- **Descripción**: Lanza los dados en la partida y actualiza los puntajes de cada jugador.
- **Parámetros**: 
  - `partida_id` (int): ID de la partida.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "mensaje": "Dados lanzados en la partida 1",
    "puntajes": {
      "jugador1": 4,
      "jugador2": 5
    }
  }
  ```
- **Errores**:
  - `404`: Partida no encontrada.
  ```json
  {
    "detail": "Partida no encontrada"
  }
  ```

### 4. **Obtener Estadísticas**
- **URL**: `/partidas/{partida_id}/estadisticas`
- **Método**: `GET`
- **Descripción**: Obtiene las estadísticas de una partida específica, incluyendo los puntajes de los jugadores.
- **Parámetros**:
  - `partida_id` (int): ID de la partida.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "partida_id": 1,
    "puntajes": {
      "jugador1": 10,
      "jugador2": 15
    }
  }
  ```
- **Errores**:
  - `404`: Partida no encontrada.
  ```json
  {
    "detail": "Partida no encontrada"
  }
  ```

### 5. **Root**
- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Punto de entrada de la API. Devuelve un mensaje de bienvenida.
- **Respuesta Exitosa (200)**:
  ```json
  {
    "message": "Bienvenido al Juego de Dados"
  }
  ```

## Ejemplos de Solicitudes y Respuestas

### Crear Partida
- **Solicitud**:
  ```bash
  curl -X POST "http://localhost:8000/partidas/" -H "Content-Type: application/json" -d '[{"nombre": "jugador1"}, {"nombre": "jugador2"}]'
  ```
- **Respuesta**:
  ```json
  {
    "mensaje": "Partida 1 creada con éxito",
    "partida": {
      "id": 1,
      "jugadores": [
        {"nombre": "jugador1"},
        {"nombre": "jugador2"}
      ],
      "puntajes": {
        "jugador1": 0,
        "jugador2": 0
      }
    }
  }
  ```

### Lanzar Dados
- **Solicitud**:
  ```bash
  curl -X POST "http://localhost:8000/partidas/1/lanzar"
  ```
- **Respuesta**:
  ```json
  {
    "mensaje": "Dados lanzados en la partida 1",
    "puntajes": {
      "jugador1": 4,
      "jugador2": 5
    }
  }
  ```

## Manejo de Errores

- La API devuelve un error `400` si:
  - El jugador ya está registrado.
  - Se intenta crear una partida con menos de dos jugadores.
- La API devuelve un error `404` si:
  - No se encuentra la partida solicitada.

Ejemplo de error:
```json
{
  "detail": "Partida no encontrada"
}
```

## Monitoreo y Métricas

- **Tiradas Totales**: Contador de todas las tiradas realizadas en las partidas. Métrica disponible a través de Prometheus (`tiradas_totales`).
- **Latencia de la API**: Histograma que mide la latencia de la API en segundos (`latencia_api`).

## Ejecución de la API

Para ejecutar la API, asegúrate de tener `uvicorn` instalado y corre el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto iniciará la aplicación en `http://localhost:8000` y expondrá las métricas en `http://localhost:8000/metrics`.


Aquí tienes la sección de ejecución de la API con la explicación de las clases, cómo se almacenan los datos, y el propósito de cada dependencia:
## Explicación de las Clases y Almacenamiento de Datos

### Clases Definidas

- **Jugador (BaseModel)**:
  Representa un jugador con un solo atributo:
  - `nombre`: El nombre del jugador, de tipo `str`.

  Ejemplo:
  ```json
  {
    "nombre": "Juan"
  }
  ```

- **Partida (BaseModel)**:
  Representa una partida de dados con tres atributos:
  - `id`: Un identificador único para la partida, de tipo `int`.
  - `jugadores`: Una lista de jugadores registrados para la partida.
  - `puntajes`: Un diccionario que asigna el nombre del jugador a su puntaje actual.

  Ejemplo:
  ```json
  {
    "id": 1,
    "jugadores": [
      {"nombre": "Juan"},
      {"nombre": "Pedro"}
    ],
    "puntajes": {
      "Juan": 0,
      "Pedro": 0
    }
  }
  ```

### Almacenamiento de Datos

La API utiliza dos listas en memoria para almacenar la información de jugadores y partidas:

- **`jugadores_registrados`**: Lista donde se almacenan todos los jugadores registrados. Cada elemento es una instancia de la clase `Jugador`.
- **`partidas`**: Lista donde se almacenan las partidas creadas. Cada elemento es una instancia de la clase `Partida`, que incluye la lista de jugadores y sus puntajes.

Ejemplo de contenido:
```python
jugadores_registrados = [Jugador(nombre="Juan")]
partidas = [
    Partida(
        id=1,
        jugadores=[Jugador(nombre="Juan"), Jugador(nombre="Pedro")],
        puntajes={"Juan": 0, "Pedro": 0}
    )
]
```

### Manejo de Estado

Los datos se mantienen en la memoria del servidor mientras la aplicación esté en ejecución. Si el servidor se reinicia, los datos se perderán, ya que no se usa una base de datos persistente, este problema se puede abordar en otra versión de nuestro proyecto. 

---

## Explicación de las Dependencias

- **FastAPI**: Framework web para construir APIs rápidas y sencillas con Python, soporta validación automática de datos y documentación de API integrada (Swagger y OpenAPI).

- **Pydantic**: Se utiliza para definir modelos de datos (como `Jugador` y `Partida`) con validación automática. Cada modelo hereda de `BaseModel` de Pydantic, lo que facilita el manejo y validación de datos.

- **Uvicorn**: Un servidor ASGI liviano que permite ejecutar aplicaciones FastAPI. El comando `uvicorn main:app --reload` inicia el servidor de desarrollo y activa la recarga automática cuando se detectan cambios en el código.

- **Prometheus FastAPI Instrumentator**: Instrumenta la API para monitoreo, permitiendo capturar métricas como el número de tiradas de dados y la latencia de las solicitudes. Las métricas se exponen en el endpoint `/metrics`.

- **Prometheus Client (Counter, Histogram)**: 
  - `Counter`: Contador para registrar el número total de tiradas de dados.
  - `Histogram`: Registro de la latencia de las solicitudes HTTP a la API.
- **Random**: Se utiliza para generar tiradas de dados aleatorias en el rango de 1 a 6 para cada jugador.

---
