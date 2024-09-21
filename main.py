import uvicorn
def jugar_consola():
    print("Bienvenido al Juego de Dados Competitivo")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    jugar_consola()
