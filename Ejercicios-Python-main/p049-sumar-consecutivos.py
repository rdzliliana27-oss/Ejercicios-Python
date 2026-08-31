# ➕ Ejercicio: suma de números consecutivos


def main():
    print("➕ --- Suma de números consecutivos ---")

    total = 0
    numero = 1
    limite = 10

    while numero <= limite:
        total += numero
        numero += 1

    print(f"✅ La suma de los números del 1 al {limite} es: {total}")


if __name__ == "__main__":
    main()
