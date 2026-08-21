import math


def main():
    print("===== HIPOTENUSA DE UN TRIANGULO =====")

    cateto1 = float(input("Ingrese la longitud del primer cateto: "))
    cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

    if cateto1 <= 0 or cateto2 <= 0:
        print("Los catetos deben ser mayores que 0.")
        return

    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")


if __name__ == "__main__":
    main()
