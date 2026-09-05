# Imprime los numeros impares desde 1 hasta un limite y calcula su suma.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                limite = int(input("Introduce un numero limite: "))
            except ValueError:
                print("Error: introduce un numero entero.")
                continue

            if limite >= 1:
                break
            print("Error: el limite debe ser mayor o igual que 1.")

        numero = 1
        suma = 0
        impares = ""
        while numero <= limite:
            if numero % 2 != 0:
                if impares != "":
                    impares += ", "
                impares += str(numero)
                suma += numero
            numero += 1

        print(f"Numeros impares: {impares}")
        print(f"La suma de los impares es: {suma}")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
