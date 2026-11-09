# Obtiene los números mayores al promedio de una lista


# Calcula y devuelve el promedio de los números de la lista.
def promedio_lista(lista: list[float]) -> float:
    # Si la lista está vacía, devuelve cero para evitar dividir entre cero.
    if not lista:
        return 0.0
    # Acumula los elementos para calcular el promedio.
    suma = 0.0
    for numero in lista:
        suma += numero
    # Divide la suma entre la cantidad de números.
    return suma / len(lista)


# Devuelve los números de la lista que son mayores que su promedio.
def mayores_al_promedio(lista: list[float]) -> list[float]:
    # Calcula primero el promedio de todos los elementos.
    promedio = promedio_lista(lista)
    # Prepara una lista para guardar los valores mayores al promedio.
    mayores = []
    # Revisa cada número de la lista.
    for numero in lista:
        if numero > promedio:
            mayores.append(numero)
    # Devuelve los números seleccionados.
    return mayores


# Función principal que demuestra cómo encontrar valores sobre el promedio.
def main() -> None:
    # Define una lista de números de ejemplo.
    numeros = [1.5, 2.3, 3.7, 4.0, 5.5]
    # Obtiene los números que superan el promedio.
    resultado = mayores_al_promedio(numeros)
    # Muestra el resultado en pantalla.
    print(f"Números mayores al promedio: {resultado}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
