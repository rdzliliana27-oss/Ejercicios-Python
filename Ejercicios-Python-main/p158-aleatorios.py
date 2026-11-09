# Genera dos listas aleatorias y suma sus elementos correspondientes

import random


# Genera y devuelve una lista con n enteros aleatorios entre minimo y maximo.
def generar_numeros_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    # Valida que la cantidad solicitada no sea negativa.
    if n < 0:
        raise ValueError("La cantidad de números no puede ser negativa.")
    # Valida que el rango de números esté en el orden correcto.
    if minimo > maximo:
        raise ValueError("El mínimo no puede ser mayor que el máximo.")
    # Prepara una lista vacía para los números generados.
    numeros_aleatorios = []
    # Genera n números dentro del rango indicado, incluyendo sus extremos.
    for _ in range(n):
        numeros_aleatorios.append(random.randint(minimo, maximo))
    # Devuelve la lista generada.
    return numeros_aleatorios


# Suma los elementos que ocupan la misma posición en dos listas iguales.
def sumar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    # Las listas deben tener igual cantidad de elementos para sumarse.
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud.")
    # Prepara una lista para guardar cada suma.
    suma = []
    # Recorre simultáneamente ambas listas y suma cada par de valores.
    for numero1, numero2 in zip(lista1, lista2):
        suma.append(numero1 + numero2)
    # Devuelve las sumas calculadas.
    return suma


# Función principal que genera dos listas aleatorias y muestra sus sumas.
def main() -> None:
    # Genera la primera lista con números entre 1 y 10.
    lista1 = generar_numeros_aleatorios(5, 1, 10)
    # Genera la segunda lista con números entre 50 y 100.
    lista2 = generar_numeros_aleatorios(5, 50, 100)
    # Suma los valores que corresponden a la misma posición.
    lista3 = sumar_listas(lista1, lista2)
    # Muestra las dos listas y la lista de resultados.
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Suma de listas: {lista3}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
