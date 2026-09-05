# Lee numeros hasta recibir 0 y muestra el conteo, la suma y el promedio.


def main():
    continuar = "S"
    while continuar == "S":
        cantidad = 0
        suma = 0
        print("Introduce numeros (0 para terminar):")

        while True:
            try:
                numero = float(input("> "))
            except ValueError:
                print("Error: introduce un numero.")
                continue

            if numero == 0:
                break
            cantidad += 1
            suma += numero

        print("-" * 20)
        print(f"Se introdujeron {cantidad} numeros.")
        print(f"La suma es: {suma:g}")
        if cantidad > 0:
            print(f"El promedio es: {suma / cantidad}")
        else:
            print("El promedio no se puede calcular porque no hay numeros.")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
