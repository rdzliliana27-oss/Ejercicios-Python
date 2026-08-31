# ✨ Ejercicio: múltiplos usando continue


def main():
    print("✨ --- Múltiplos de 3 del 1 al 30 (sin 15) ---")

    numero = 1

    while numero <= 30:
        if numero % 3 != 0 or numero == 15:
            numero += 1
            continue

        print(f"✨ {numero}")
        numero += 1


if __name__ == "__main__":
    main()
