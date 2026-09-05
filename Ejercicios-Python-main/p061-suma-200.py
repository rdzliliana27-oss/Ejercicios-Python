# Lee numeros hasta alcanzar o superar una suma acumulada de 200.


def main():
    continuar = "S"
    while continuar == "S":
        suma = 0
        cantidad = 0

        while suma < 200:
            try:
                numero = float(input(f"Suma actual: {suma:g}. Introduce un numero: "))
            except ValueError:
                print("Error: introduce un numero.")
                continue

            suma += numero
            cantidad += 1

        print("-" * 20)
        print("Meta de 200 alcanzada.")
        print(f"Suma final: {suma:g}")
        print(f"Total de numeros introducidos: {cantidad}")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
