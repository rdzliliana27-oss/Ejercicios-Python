
## Conversor de Temperaturas
##    Convierte entre Celsius, Fahrenheit y Kelvin. 


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_a_kelvin(fahrenheit):
    celsius = fahrenheit_a_celsius(fahrenheit)
    return celsius_a_kelvin(celsius)


def kelvin_a_celsius(kelvin):
    return kelvin - 273.15


def kelvin_a_fahrenheit(kelvin):
    celsius = kelvin_a_celsius(kelvin)
    return celsius_a_fahrenheit(celsius)


def pedir_temperatura():
    """Pide un valor numérico al usuario, validando la entrada."""
    while True:
        try:
            return float(input("Ingresa el valor de temperatura: "))
        except ValueError:
            print("Entrada inválida. Escribe un número (ej: 25.5).\n")


def mostrar_menu():
    print("\n------- CONVERSOR DE TEMPERATURA -------")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Fahrenheit a Kelvin")
    print("5. Kelvin a Celsius")
    print("6. Kelvin a Fahrenheit")
    print("0. Salir")
    print("__________________________________________")


def main():
    opciones = {
        "1": ("°C -> °F", celsius_a_fahrenheit, "°F"),
        "2": ("°C -> K", celsius_a_kelvin, "K"),
        "3": ("°F -> °C", fahrenheit_a_celsius, "°C"),
        "4": ("°F -> K", fahrenheit_a_kelvin, "K"),
        "5": ("K -> °C", kelvin_a_celsius, "°C"),
        "6": ("K -> °F", kelvin_a_fahrenheit, "°F"),
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion not in opciones:
            print("Opción no válida, intenta de nuevo.\n")
            continue

        etiqueta, funcion, unidad_salida = opciones[opcion]
        valor = pedir_temperatura()
        resultado = funcion(valor)
        print(f"\nResultado ({etiqueta}): {resultado:.2f} {unidad_salida}\n")


if __name__ == "__main__":
    main()
