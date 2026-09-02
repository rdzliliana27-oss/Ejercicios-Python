# 🔢 Calcula la conjetura de Collatz.


def main():
    while True:
        while True:
            try:
                numero = int(input("Dame un numero entero positivo: "))
            except ValueError:
                print("Error: introduce un numero entero.")
                continue

            if numero > 0:
                break
            print("Error: el numero debe ser mayor que 0.")

        print("\n🔁 La conjetura de Collatz es:")
        while numero != 1:
            print(numero, end=" ")
            if numero % 2 == 0:
                numero //= 2
            else:
                numero = numero * 3 + 1
        print(1)

        if input("\nDeseas continuar (S/N)? ").strip().upper() == "N":
            break

    print("\n✅ Gracias por usar este programa.")


if __name__ == "__main__":
    main()
