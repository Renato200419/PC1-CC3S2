# Documentación de Docker y Docker Compose
## Introducción
En este proyecto utilizamos Docker y Docker Compose para contenerizar la aplicación del juego de dados, así como los servicios adicionales de Prometheus y Grafana para monitoreo. Esto permite una fácil configuración y ejecución de todos los servicios necesarios en un entorno controlado y replicable.
## Estructura de los Servicios
El proyecto contiene los siguientes servicios dentro de contenedores:
- **app**: Contenedor que ejecuta la API REST del juego de dados desarrollada en Python usando FastAPI.
- **prometheus**: Contenedor que ejecuta Prometheus para recolectar métricas de la API.
- **grafana**: Contenedor que ejecuta Grafana para visualizar las métricas recolectadas por Prometheus.

## Pasos que se realizaron:
1. Al iniciar el repositorio se creó la rama `feature/estructura-básica` en el cual se agregó el Dockerfile.
### Dockerfile
```bash
# Usamos la imagen base de Python 3.8
FROM python:3.8
# Copiamos el contenido del directorio 'app' en el contenedor en la ruta '/app'
COPY ./app /app
# Establecemos el directorio de trabajo en '/app'
WORKDIR /app
# Instalamos las dependencias necesarias: FastAPI y Uvicorn
RUN pip install fastapi uvicorn
# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Luego se hizo una modificación en la línea de COPY en la misma rama:

```bash
# Copiamos todos los archivos del directorio actual al contenedor en la ruta '/app'
COPY . /app
```
3. También se agrega la estructura básica del docker-compose.yml:
```bash
version: '3.8'  # Usa la versión 3.8 de Docker Compose
services:
  app:  # Nombre del servicio
    build: .  # Construye la imagen a partir del Dockerfile en el directorio actual
    ports:
      - "8000:8000"  # Mapea el puerto 8000 del contenedor al puerto 8000 del host
    environment:
      - ENVIRONMENT=production  # Define una variable de entorno
    volumes:
      - .:/app  # Monta el directorio actual en '/app' dentro del contenedor
    command: uvicorn app:app --host 0.0.0.0 --port 8000  # Comando para ejecutar la aplicación
```
4. Posteriormente modificamos el docker-compose.yml en el cual se incluye la configuración de Prometheus y Grafana:

```bash
version: '3.8'

services:
  app:
    build: .  # Construye la imagen desde el Dockerfile en el directorio actual
    ports:
      - "8000:8000"  # Mapea el puerto 8000 del contenedor al puerto 8000 del host
    environment:
      - ENVIRONMENT=production  # Establece la variable de entorno para indicar que es producción
    volumes:
      - .:/app  # Monta el directorio actual en /app dentro del contenedor
    command: uvicorn app:app --host 0.0.0.0 --port 8000  # Comando para iniciar la aplicación usando Uvicorn

  prometheus:
    image: prom/prometheus  # Utiliza la imagen oficial de Prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml  # Monta el archivo de configuración de Prometheus
    ports:
      - "9090:9090"  # Mapea el puerto 9090 del contenedor al puerto 9090 del host
    depends_on:
      - app  # Asegura que el servicio 'app' esté en ejecución antes de iniciar Prometheus

  grafana:
    image: grafana/grafana  # Utiliza la imagen oficial de Grafana
    ports:
      - "3000:3000"  # Mapea el puerto 3000 del contenedor al puerto 3000 del host
    depends_on:
      - prometheus  # Asegura que Prometheus esté en ejecución antes de iniciar Grafana
    environment:
      - GF_USERS_ALLOW_SIGN_UP=false  # Desactiva el registro de nuevos usuarios

volumes:
  grafana_data:
    driver: local  # Define un volumen local para almacenar datos de Grafana
```

5. Se hizo cambios en `requirements.txt` ya que se presentó un error en la compilación del main.py
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
```
6. Luego modificamos el Dockerfile añadiendo `requirements.txt` para actualizar la forma en la que se instalan las dependencias:
```bash
# Usamos la imagen base de Python 3.8
FROM python:3.8

# Copiamos todos los archivos del directorio actual al contenedor en la ruta '/app'
COPY . /app

# Establecemos el directorio de trabajo en '/app'
WORKDIR /app
COPY requirements.txt ./

# Instalamos las dependencias necesarias: FastAPI y Uvicorn
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

7. Finalmente actualizamos el docker-compose.yml en el cual se modifica para mantener los datos intactos:
```bash
version: '3.8'

services:
  app:
    build: .  # Construye la imagen desde el Dockerfile en el directorio actual
    ports:
      - "8000:8000"  # Mapea el puerto 8000 del contenedor al puerto 8000 del host
    environment:
      - ENVIRONMENT=production  # Establece la variable de entorno para indicar que es producción
    volumes:
      - .:/app  # Monta el directorio actual en /app dentro del contenedor
    command: uvicorn app:app --host 0.0.0.0 --port 8000  # Comando para iniciar la aplicación usando Uvicorn

  prometheus:
    image: prom/prometheus  # Utiliza la imagen oficial de Prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml  # Monta el archivo de configuración de Prometheus
      - prometheus_data:/prometheus  # Almacena datos de series temporales aquí
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
  grafana_data:
    driver: local  # Define un volumen local para almacenar datos de Grafana
  prometheus_data:
    driver: local  # Define un volumen local para almacenar datos de Prometheus
```
## Ejecución del Proyecto con Docker Compose

### 1. Iniciar los Servicios
Para iniciar todos los servicios (API, Prometheus y Grafana), ejecutar el siguiente comando:
```bash
docker-compose up --build
```
### 2. Detener los Servicios
Para detener todos los servicios, usar:
```bash
docker-compose down
```

### 3. Reconstruir los Contenedores
Si se realiza cambios en el código o en las configuraciones, usamos el mismo comando del paso 1 para  reconstruir los contenedores con:

```bash
docker-compose up --build
```
### 4. Verificar los Contenedores Corriendo
Para verificar que todos los contenedores están corriendo:

```bash
docker ps
```

## Acceso a los Servicios
Una vez que los contenedores estén en funcionamiento, podemos acceder a los servicios en los siguientes enlaces:

- **API del Juego**: [http://localhost:8000](http://localhost:8000)
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000)

## Uso de Volúmenes
Para asegurar que los datos de Grafana y Prometheus no se pierdan entre reinicios de contenedores, se configuraron los siguientes volúmenes.

### 1. Volumen de Grafana
- **`grafana_data`**: Se utiliza para almacenar los dashboards y configuraciones de Grafana.
```yaml
volumes:
  grafana_data:
    driver: local
```
### 2. Volumen de Prometheus
`prometheus_data`: Almacena los datos históricos de métricas recolectadas por Prometheus.
 ```yaml
volumes:
  prometheus_data:
    driver: local
 ```
## Finalización con `pull request` y la aceptación del `merge`
1. Al subir los cambios en la rama, se hace un `Compare & pull request`
2. Se añade un título y una descripción breve.
3. Luego se agrega un comentario avisando que estás esperando la aceptación de los cambios. [optional]
4. Uno de los colaboradores acepta nuestros cambios.

![Descripción de la imagen](Imagenes/Imagen.png)
