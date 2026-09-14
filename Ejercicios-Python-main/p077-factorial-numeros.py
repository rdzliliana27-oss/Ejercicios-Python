# 🧮 Calcula los factoriales desde 1 hasta n usando un ciclo for.

import sys


sys.stdout.reconfigure(encoding="utf-8")


def main():
    while True:
        try:
            limite = int(input("🔢 ¿Hasta qué número calculamos factoriales? "))
            if limite < 1:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Introduce un entero positivo.")

    factorial = 1
    for numero in range(1, limite + 1):
        factorial *= numero
        print(f"{numero}! = {factorial}")

    print("✅ Cálculo terminado.")


if __name__ == "__main__":
    main()
