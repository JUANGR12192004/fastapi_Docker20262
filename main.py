from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/obtener_cedula")
def obtener_cedula():
    """Devuelve un número entero aleatorio de 10 dígitos bajo la clave 'cedula'."""
    numero = random.randint(10**9, 10**10 - 1)
    return {"cedula": numero}
