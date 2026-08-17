
##    p007-entrada-multiple.py
##    Conversor de temperaturas con entrada múltiple.
##    Convierte varios valores de una sola vez, separados por coma.



def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius):
    return celsius + 273.15


CONVERSIONES = {
    "1": ("Celsius a Fahrenheit", celsius_a_fahrenheit, "°F"),
    "2": ("Celsius a Kelvin", celsius_a_kelvin, "K"),
}


def leer_valores_multiples(texto):
    """
        Recibe un texto como '20, 25, 30' y regresa una lista de floats.
        Ignora espacios y valores que no se puedan convertir.
    """
    valores = []
    for pedazo in texto.split(","):
        pedazo = pedazo.strip()
        if pedazo == "":
            continue
        try:
            valores.append(float(pedazo))
        except ValueError:
            print(f"Se ignoró '{pedazo}' porque no es un número válido.")
    return valores


def convertir_lista(valores, funcion_conversion):
    """Aplica la función de conversión a cada valor de la lista."""
    return [funcion_conversion(valor) for valor in valores]


def mostrar_menu():
    print("\n===== CONVERSOR DE TEMPERATURA (ENTRADA MÚLTIPLE) =====")
    for clave, (etiqueta, _, _) in CONVERSIONES.items():
        print(f"{clave}. {etiqueta}")
    print("0. Salir")
    print("=========================================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion not in CONVERSIONES:
            print("Opción no válida, intenta de nuevo.\n")
            continue

        etiqueta, funcion, unidad_salida = CONVERSIONES[opcion]

        texto_entrada = input("Escribe los valores separados por coma (ej: 20, 25, 30): ")
        valores = leer_valores_multiples(texto_entrada)

        if not valores:
            print("No se ingresó ningún valor válido.\n")
            continue

        resultados = convertir_lista(valores, funcion)

        print(f"\nResultados ({etiqueta}):")
        for original, resultado in zip(valores, resultados):
            print(f"  {original} -> {resultado:.2f} {unidad_salida}")
        print()


if __name__ == "__main__":
    main()