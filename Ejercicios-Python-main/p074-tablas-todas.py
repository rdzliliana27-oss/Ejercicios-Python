# 🐱‍💻 Muestra las tablas de multiplicar usando ciclos for anidados.

import sys
sys.stdout.reconfigure(encoding="utf-8")


def main():
    print("🐱 ¡Hola! Vamos a practicar las tablas.")
    print(" /\\_/\\\\")
    print("( o.o )")
    print(" > ^ <\n")

    while True:
        try:
            limite = int(input("📚 ¿Hasta qué tabla deseas llegar? "))
            if limite < 1:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Introduce un entero positivo.")

    for tabla in range(1, limite + 1):
        print(f"\n✏️ Tabla del {tabla}")
        for multiplicador in range(1, 11):
            print(f"{tabla:2} × {multiplicador:2} = {tabla * multiplicador:3}")

    print("\n🎉 ¡Todas las tablas están listas!")


if __name__ == "__main__":
    main()
