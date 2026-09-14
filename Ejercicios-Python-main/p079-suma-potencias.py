# ➕ Calcula la suma de potencias de 1 hasta n.

import sys


sys.stdout.reconfigure(encoding="utf-8")


def main():
    while True:
        try:
            limite = int(input("🔢 ¿Cuál es el valor de n? "))
            exponente = int(input("⚡ ¿Qué exponente deseas usar? "))
            if limite < 1 or exponente < 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ n debe ser positivo y el exponente no puede ser negativo.")

    suma = 0
    terminos = []
    for numero in range(1, limite + 1):
        potencia = numero ** exponente
        suma += potencia
        terminos.append(str(potencia))

    print(f"\n📐 Suma: {' + '.join(terminos)}")
    print(f"✅ Resultado: {suma}")


if __name__ == "__main__":
    main()
