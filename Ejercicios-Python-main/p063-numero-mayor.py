# Lee numeros hasta recibir 0 y muestra el mayor de la serie.


def main():
    continuar = "S"
    while continuar == "S":
        mayor = None
        print("Introduce numeros (0 para terminar):")

        while True:
            try:
                numero = float(input("> "))
            except ValueError:
                print("Error: introduce un numero.")
                continue

            if numero == 0:
                break
            if mayor is None or numero > mayor:
                mayor = numero

        print("-" * 20)
        if mayor is None:
            print("No se introdujeron numeros.")
        elif mayor.is_integer():
            print(f"El numero mayor fue: {int(mayor)}")
        else:
            print(f"El numero mayor fue: {mayor:g}")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
