def main():
    print("===== TERCER ANGULO DE UN TRIANGULO =====")

    angulo1 = float(input("Ingrese el primer angulo: "))
    angulo2 = float(input("Ingrese el segundo angulo: "))
    angulo3 = 180 - (angulo1 + angulo2)

    if angulo1 <= 0 or angulo2 <= 0 or angulo3 <= 0:
        print("Los angulos deben ser positivos y su suma debe ser menor que 180 grados.")
        return

    print(f"El tercer angulo mide: {angulo3:.2f} grados")


if __name__ == "__main__":
    main()
