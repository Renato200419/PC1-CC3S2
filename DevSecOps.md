
---
# DevSecOps

## Propósito

El propósito de esta documentación es explicar cómo se ha implementado DevSecOps en el proyecto, integrando prácticas de desarrollo, seguridad y operaciones (DevSecOps) para asegurar que el ciclo de vida del software sea seguro, eficiente y automatizado. Se detalla cómo la seguridad se integra en cada fase del pipeline de CI/CD, desde la instalación de dependencias hasta la auditoría de vulnerabilidades.

## 1. Configuración de análisis de seguridad

### Herramientas de auditoría

Para garantizar la seguridad del código, se ha integrado la siguiente herramienta en el pipeline CI/CD:

- **pip-audit**: Una herramienta que audita las dependencias del proyecto para detectar vulnerabilidades conocidas en paquetes de Python.

Esta herramienta se ejecuta automáticamente cada vez que se realizan cambios en el código, alertando al equipo si existen vulnerabilidades que podrían poner en riesgo el proyecto.

### Ejecución de auditorías de seguridad

La auditoría de seguridad se realiza a través de la herramienta **pip-audit** en el pipeline de GitHub Actions. Esta herramienta analiza las dependencias en el archivo `requirements.txt` para identificar cualquier vulnerabilidad conocida:

```bash
pip-audit
```

Cada vez que se realiza un push o pull request en la rama `main`, el pipeline CI/CD ejecuta esta auditoría. En caso de encontrar una vulnerabilidad, el pipeline falla, alertando a los desarrolladores para que solucionen el problema antes de proceder con el despliegue.

Ejemplo de como **pip-audit** detecta vulnerabilidades y falla el pipeline:
- Alerta en el pipeline:
	
	![[pip-audit.png]](Imagenes/pip-audit.png)
	
- Medidas tomadas:
	
	![[medidas.png]](Imagenes/medidas.png)

---

## 2. Configuración de GitHub Actions para CI/CD

El archivo `ci.yml` define las diferentes etapas del pipeline DevSecOps. Este es el código de `ci.yml` que fue construyendose poco a poco a lo largo de nuestro proyecto:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install --upgrade setuptools
          pip install -r requirements.txt

      - name: Run tests
        env:
          PYTHONPATH: .
        run: |
            pytest tests/

      - name: Install pip-audit
        run: pip install pip-audit

      - name: Audit dependencies
        run: pip-audit

      - name: Build Docker image
        run: docker build -t juego-dados-competitivo .

      - name: Run Docker container
        run: docker run -d -p 8000:8000 juego-dados-competitivo

      - name: Wait for FastAPI to be ready
        run: |
          until curl -s http://localhost:8000/; do
            echo "Esperando a que FastAPI esté disponible..."
            sleep 5
          done
```

Este archivo de pipeline realiza las siguientes tareas:

1. **Checkout del código**: Descarga el código desde el repositorio de GitHub.
2. **Instalación de Python**: Configura el entorno de Python en la versión 3.8.
3. **Instalación de dependencias**: Instala las dependencias del proyecto especificadas en `requirements.txt`.
4. **Ejecución de pruebas**: Ejecuta los tests automáticos definidos en el directorio `tests/` utilizando `pytest`.
5. **Auditoría de dependencias con `pip-audit`**: Ejecuta la herramienta `pip-audit` para identificar posibles vulnerabilidades en las dependencias del proyecto.
6. **Construcción de imagen Docker**: Construye una imagen Docker para la aplicación.
7. **Despliegue en Docker**: Inicia un contenedor Docker con la aplicación FastAPI.
8. **Espera de FastAPI**: Espera hasta que el servidor FastAPI esté disponible.

---
## 3. Instrucciones para ejecutar auditorías de seguridad manualmente

Si deseas ejecutar la auditoría de seguridad de forma manual sin esperar a que se active el pipeline CI/CD, sigue estos pasos:

1. Asegúrate de tener **pip-audit** instalado:
   
   ```bash
   pip install pip-audit
   ```

2. Ejecuta la auditoría de seguridad con el siguiente comando:

   ```bash
   pip-audit
   ```

Esto generará un informe que detallará cualquier vulnerabilidad detectada en las dependencias del proyecto. En caso de encontrar alguna, actualiza las dependencias afectadas o considera opciones alternativas que sean más seguras.

---

## 4. Reflexión sobre el impacto del Sec en DevSecOps

La inclusión de **seguridad** en el pipeline (Sec en DevSecOps) asegura que el software no solo sea funcional, sino también seguro desde las primeras etapas del desarrollo. Al integrar **pip-audit** en el pipeline CI/CD, hemos logrado un enfoque proactivo para la seguridad. Esto significa que cualquier vulnerabilidad en las dependencias será detectada y reportada antes de que el código se despliegue en producción, permitiendo que el equipo reaccione rápidamente.

Este enfoque mejora significativamente la postura de seguridad del proyecto, ya que permite identificar y remediar problemas de seguridad antes de que afecten al usuario final.

---

### 5. Reflexión final sobre el flujo de trabajo DevSecOps

El enfoque DevSecOps utilizado en este proyecto combina desarrollo, seguridad y operaciones de manera efectiva, asegurando que todas las etapas del ciclo de vida del software se gestionen de forma automatizada y segura. Los beneficios principales de esta implementación han sido:

- **Automatización**: Nos ha permitido reducir el tiempo necesario para realizar pruebas y auditorías, y eliminar tareas repetitivas.
- **Seguridad proactiva**: Las vulnerabilidades se detectan y gestionan automáticamente antes de que lleguen a producción.
- **Entrega continua**: El uso de Docker facilita la consistencia entre los entornos de desarrollo y producción, lo que acelera la entrega de nuevas versiones del software.

El flujo DevSecOps asegura una entrega continua con altos estándares de seguridad y eficiencia, lo que no solo mejora la calidad del software, sino que también incrementa la confianza del equipo y de los usuarios en el producto final.