from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .database import initialize_db
from .routes import router

import uvicorn

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir las rutas desde el router
app.include_router(router)

# Instrumentar la aplicación y exponer las métricas
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Inicializar la base de datos en el evento de inicio de la aplicación
@app.on_event("startup")
def startup_event():
    initialize_db()

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Juego de Dados"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
