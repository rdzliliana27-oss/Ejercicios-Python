# Separa una lista de números en pares e impares


# Recibe una lista y devuelve dos listas: pares e impares.
def separar_pares_impares(
    lista: list[int],
) -> tuple[list[int], list[int]]:
    # Prepara una lista para cada tipo de número.
    pares = []
    impares = []
    # Revisa cada número de la lista recibida.
    for numero in lista:
        # Si el residuo al dividir entre dos es cero, el número es par.
        if numero % 2 == 0:
            pares.append(numero)
        # Los números que no son pares se guardan como impares.
        else:
            impares.append(numero)
    # Devuelve ambas listas, primero los pares y luego los impares.
    return pares, impares


# Función principal que demuestra cómo separar los números.
def main() -> None:
    # Define una lista de enteros de ejemplo.
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Recibe las dos listas que devuelve la función.
    pares, impares = separar_pares_impares(numeros)
    # Muestra cada lista y cuántos elementos contiene.
    print(f"Números pares: {pares} - fueron: {len(pares)}")
    print(f"Números impares: {impares} - fueron: {len(impares)}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
