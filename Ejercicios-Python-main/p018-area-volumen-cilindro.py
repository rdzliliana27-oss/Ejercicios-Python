import math


def main():
    print("===== AREA Y VOLUMEN DE UN CILINDRO =====")

    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))

    if radio <= 0 or altura <= 0:
        print("El radio y la altura deben ser mayores que 0.")
        return

    area = 2 * math.pi * radio * (radio + altura)
    volumen = math.pi * radio ** 2 * altura

    print(f"El area total del cilindro es: {area:.2f} unidades cuadradas")
    print(f"El volumen del cilindro es: {volumen:.2f} unidades cubicas")


if __name__ == "__main__":
    main()
