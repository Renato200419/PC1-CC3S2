# Usamos la imagen base de Python 3.8
FROM python:3.8

# Copiamos todos los archivos del directorio actual al contenedor en la ruta '/app'
COPY . /app

# Establecemos el directorio de trabajo en '/app'
WORKDIR /app

# Instalamos las dependencias necesarias: FastAPI y Uvicorn
RUN pip install fastapi uvicorn

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
