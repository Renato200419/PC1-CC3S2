from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .database import initialize_db
from .routes import router  # Importar el enrutador de rutas

import uvicorn

# Crear la aplicación FastAPI
app = FastAPI()

# Inicializar la base de datos
initialize_db()

# Inicializar el instrumentador para Prometheus
instrumentator = Instrumentator()

# Incluir las rutas desde el router
app.include_router(router)

# Instrumentar la aplicación y exponer las métricas
instrumentator.instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Juego de Dados"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)