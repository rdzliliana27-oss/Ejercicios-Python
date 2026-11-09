# Suma los elementos de una lista de números


# Recibe una lista de números y devuelve la suma de sus elementos.
def suma_lista(lista: list[float]) -> float:
    # Inicia la suma en cero.
    suma = 0.0
    # Recorre los números de la lista y los acumula.
    for numero in lista:
        suma += numero
    # Devuelve el total calculado.
    return suma


# Función principal que demuestra cómo usar suma_lista.
def main() -> None:
    # Define una lista de números de ejemplo.
    numeros = [1.5, 2.3, 3.7, 4.0]
    # Calcula la suma de los números.
    resultado = suma_lista(numeros)
    # Muestra el resultado en pantalla.
    print(f"La suma de la lista es: {resultado}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
