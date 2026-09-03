from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/obtener_cedula")
def obtener_cedula():
    """Devuelve un número entero aleatorio de 10 dígitos bajo la clave 'cedula'."""
    numero = random.randint(10**9, 10**10 - 1)
    return {"cedula": numero}


def int_to_roman(num: int) -> str:
    """Convierte un entero (1..3999) a número romano.

    Implementación simple usando pares valor-símbolo.
    """
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = []
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num.append(syms[i])
            num -= val[i]
        i += 1
    return ''.join(roman_num)


@app.get("/obtener_romano")
def obtener_romano():
    """Devuelve aleatoriamente un número romano entre 50 y 100 (inclusive)."""
    n = random.randint(50, 100)
    romano = int_to_roman(n)
    return {"numero": n, "romano": romano}


def multiplicar_por_dos(n: float) -> float:
    """Devuelve el número `n` multiplicado por 2.

    Acepta `int` o `float` y devuelve `float`.
    """
    return n * 2
