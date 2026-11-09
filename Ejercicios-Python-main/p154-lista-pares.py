# Obtiene los números pares de una lista


# Recibe una lista de enteros y devuelve otra con los números pares.
def lista_pares(lista: list[int]) -> list[int]:
    # Prepara una lista vacía para guardar los pares encontrados.
    pares = []
    # Revisa cada número de la lista original.
    for numero in lista:
        # Un número es par si el residuo al dividirlo entre dos es cero.
        if numero % 2 == 0:
            pares.append(numero)
    # Devuelve la lista de números pares.
    return pares


# Función principal que demuestra cómo usar lista_pares.
def main() -> None:
    # Define una lista de enteros de ejemplo.
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Obtiene los números pares de la lista.
    resultado = lista_pares(numeros)
    # Muestra los números pares encontrados.
    print(f"Los números pares de la lista son: {resultado}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
