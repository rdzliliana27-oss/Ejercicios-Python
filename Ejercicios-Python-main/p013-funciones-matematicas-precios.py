##    p013-funciones-matematicas-precios.py
##    Demuestra el uso de funciones matemáticas para redondear precios.

import math


def calcular_redondeos(precio: float) -> dict[str, float]:
    operaciones = {
        "Redondeo arriba": math.ceil(precio),
        "Redondeo abajo": math.floor(precio),
        "Sin decimales": math.trunc(precio),
        "Redondeo normal": round(precio),
        "Un decimal": round(precio, 1),
    }
    return operaciones


def main():
    print("===== REDONDEO DE PRECIOS =====")

    try:
        precio = float(input("Ingresa un precio con decimales: "))
    except ValueError:
        print("Ingresa un precio válido.")
        return

    if precio < 0:
        print("El precio no puede ser negativo.")
        return

    print(f"Precio original: ${precio:.2f}")
    for nombre, resultado in calcular_redondeos(precio).items():
        print(f"{nombre}: ${resultado:.2f}")


if __name__ == "__main__":
    main()
