# 🔢 Ejercicio: conteo de números pares


def main():
    print("🔢 --- Conteo de números pares ---")

    contador = 0
    numero = 1
    limite = 20

    while numero <= limite:
        if numero % 2 == 0:
            contador += 1
        numero += 1

    print(f"✅ Hay {contador} números pares del 1 al {limite}.")


if __name__ == "__main__":
    main()
