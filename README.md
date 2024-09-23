# Proyecto 9: Juego de Dados Competitivo

## Descripción del Proyecto
Este proyecto implementa un juego de dados competitivo donde los jugadores compiten por obtener la mayor puntuación. Las estadísticas del juego se almacenan en un servidor y se monitorean en tiempo real usando Prometheus y Grafana. Además, se implementa un flujo de DevSecOps con análisis de seguridad y CI/CD.

## Tecnologías Utilizadas
- **Lenguajes de Programación**: Python
- **Framework**: FastAPI para la API REST.
- **Contenerización**: Docker, Docker Compose
- **Monitoreo**: Prometheus, Grafana
- **DevSecOps**: Script de auditoría de seguridad (`audit.sh`), GitHub Actions para CI/CD

## Objetivos
1. Implementar una API REST que gestione las partidas y registre las puntuaciones de los jugadores.
2. Desarrollar un cliente de consola (en `main.py`) para que los jugadores puedan participar en las partidas.
3. Configurar un análisis de seguridad usando un script (`audit.sh`) y generar reportes de vulnerabilidades (`audit_report.txt`).
4. Usar Docker y Docker Compose para contenerizar la aplicación y gestionar los servicios.
5. Monitorear las métricas del juego como la cantidad de tiradas y la latencia de la API utilizando Prometheus y Grafana.
6. Gestionar el CI/CD mediante GitHub Actions (`.github/workflows/ci.yml`).

## Estructura del Proyecto
- **`app.py`**: Implementación principal de la API REST.
- **`main.py`**: Cliente de consola para jugar al juego de dados.
- **`docker-compose.yml`**: Archivo para orquestar los servicios de Docker.
- **`requirements.txt`**: Dependencias del proyecto.
- **`prometheus.yml`**: Configuración para Prometheus.
- **`audit.sh`**: Script de análisis de seguridad.
- **`audit_report.txt`**: Informe de seguridad generado.
- **`/Dashboard/`**: Configuraciones de métricas para Prometheus y Grafana.
- **`tests/`**: Contiene tests para verificar el correcto funcionamiento del juego.

## Guía de Instalación y Uso

### Requisitos Previos
- Docker y Docker Compose instalados.
- Acceso a una terminal.

### Instalación
1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/usuario/juego-dados-competitivo.git
2. Navega al directorio del proyecto:
   ```bash
   cd juego-dados-competitivo
3. Construye y levanta los servicios con Docker Compose:
    ```bash
   docker-compose up --build
###Uso
1. Ejecuta el cliente de consola:
   ```bash
   python main.py
2. Accede al tablero de Grafana en http://localhost:3000 para ver las métricas en tiempo real.

## Cómo Contribuir
1. Haz un fork del repositorio.
2. Crea una nueva rama
   ```bash
   git checkout -b nueva-funcionalidad.
3. Realiza los cambios necesarios y commitea
   ```bash
   git commit -m 'Añadir nueva funcionalidad'
4. Empuja los cambios a tu fork
   ```bash
   git push origin nueva-funcionalidad
6. Crea un Pull Request en GitHub, para revisión.

## Funcionalidades Futuras:
- Añadir autenticación de usuarios.
- Incluir más tipos de juegos de dados.
- Mejorar las métricas con análisis avanzados de las partidas.
