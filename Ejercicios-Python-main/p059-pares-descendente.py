# Imprime los numeros pares desde 100 hasta un limite y calcula su suma.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                limite = int(input("Introduce un numero limite (menor a 100): "))
            except ValueError:
                print("Error: introduce un numero entero.")
                continue

            if 0 <= limite < 100:
                break
            print("Error: el limite debe estar entre 0 y 99.")

        numero = 100
        suma = 0
        pares = ""
        while numero >= limite:
            if numero % 2 == 0:
                if pares != "":
                    pares += ", "
                pares += str(numero)
                suma += numero
            numero -= 1

        print(f"Numeros pares: {pares}")
        print(f"La suma de los pares es: {suma}")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
