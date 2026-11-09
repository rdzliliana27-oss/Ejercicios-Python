# Une dos listas de nombres, invierte el orden y los convierte a mayúsculas


# Recibe dos listas de nombres y devuelve una lista con los nombres procesados.
def une_procesa(lista1: list[str], lista2: list[str]) -> list[str]:
    # Junta los nombres de ambas listas, en el orden en que se recibieron.
    nombres_unidos = lista1 + lista2
    # Crea una nueva lista con los nombres en orden inverso.
    nombres_invertidos = nombres_unidos[::-1]
    # Prepara una lista vacía para guardar los nombres en mayúsculas.
    nombres_mayusculas = []
    # Recorre los nombres invertidos, uno por uno.
    for nombre in nombres_invertidos:
        # Convierte el nombre actual a mayúsculas y lo agrega a la lista.
        nombres_mayusculas.append(nombre.upper())
    # Devuelve la lista final sin cambiar las listas originales.
    return nombres_mayusculas


# Pide nombres al usuario hasta que ingrese una línea vacía.
def capturar_nombres() -> list[str]:
    # Aquí se guardarán los nombres que escriba el usuario.
    datos = []
    print("Introduce nombres (deja en blanco para terminar):")
    # Repite la pregunta hasta que se indique que ya terminó.
    while True:
        nombre = input("Nombre: ")
        # Si no se escribió nada, termina el ciclo.
        if nombre == "":
            break
        # Si se escribió un nombre, lo agrega a la lista.
        datos.append(nombre)
    # Devuelve todos los nombres capturados.
    return datos


# Función principal: organiza la captura, el procesamiento y la impresión.
def main() -> None:
    # Define la primera lista de nombres.
    nombres1 = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
    # Captura una segunda lista escrita por el usuario.
    nombres2 = capturar_nombres()
    # Une ambas listas, invierte su orden y convierte los nombres a mayúsculas.
    nombres_procesados = une_procesa(nombres1, nombres2)
    # Muestra los nombres resultantes y cuántos hay.
    print(
        f"Nombres procesados: {nombres_procesados} "
        f"- fueron: {len(nombres_procesados)}"
    )


# Ejecuta main solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
