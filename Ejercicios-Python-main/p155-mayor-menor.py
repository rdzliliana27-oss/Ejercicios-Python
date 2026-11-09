# Encuentra el mayor y el menor de una lista no vacía


# Devuelve el número más grande de la lista.
def mayor(lista: list[float]) -> float:
    # No se puede buscar un máximo si no hay elementos.
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    # Usa el primer elemento como el mayor conocido inicialmente.
    mayor_num = lista[0]
    # Compara cada número con el mayor encontrado hasta el momento.
    for numero in lista:
        if numero > mayor_num:
            mayor_num = numero
    # Devuelve el número más grande.
    return mayor_num


# Devuelve el número más pequeño de la lista.
def menor(lista: list[float]) -> float:
    # No se puede buscar un mínimo si no hay elementos.
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    # Usa el primer elemento como el menor conocido inicialmente.
    menor_num = lista[0]
    # Compara cada número con el menor encontrado hasta el momento.
    for numero in lista:
        if numero < menor_num:
            menor_num = numero
    # Devuelve el número más pequeño.
    return menor_num


# Pide números al usuario hasta que escriba "fin".
def captura_datos() -> list[float]:
    # Aquí se guardarán los números válidos.
    datos = []
    print("Ingresa números (escribe 'fin' para terminar):")
    # Continúa pidiendo datos hasta que el usuario termine.
    while True:
        entrada = input("Número: ")
        # Ignora mayúsculas y minúsculas al reconocer la palabra "fin".
        if entrada.lower() == "fin":
            break
        # Intenta convertir la entrada a un número decimal.
        try:
            numero = float(entrada)
        # Informa si la entrada no representa un número válido.
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin' para terminar.")
        # Guarda el número cuando la conversión fue exitosa.
        else:
            datos.append(numero)
    # Devuelve todos los números capturados.
    return datos


# Función principal que coordina la captura y muestra los resultados.
def main() -> None:
    # Obtiene los números escritos por el usuario.
    numeros = captura_datos()
    # Si no se capturaron números, muestra un aviso y termina.
    if not numeros:
        print("No se ingresaron números.")
        return

    # Muestra la cantidad de valores y sus extremos.
    print(f"Total de números ingresados: {len(numeros)}")
    print(f"El número mayor es: {mayor(numeros)}")
    print(f"El número menor es: {menor(numeros)}")


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
