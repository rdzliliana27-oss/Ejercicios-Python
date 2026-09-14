# 🔺 Dibuja un triángulo de caracteres usando un ciclo for.

import sys


sys.stdout.reconfigure(encoding="utf-8")


def main():
    caracter = input("🔤 ¿Qué carácter deseas usar? ").strip() or "*"

    while True:
        try:
            filas = int(input("📏 ¿Cuántas filas tendrá el triángulo? "))
            if filas < 1:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Introduce un entero positivo.")

    print("\n🔺 Triángulo:")
    for fila in range(1, filas + 1):
        print(caracter * fila)


if __name__ == "__main__":
    main()
