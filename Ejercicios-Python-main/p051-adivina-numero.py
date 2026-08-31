# 🎯 Ejercicio: adivina el número


def main():
    print("🎯 --- Adivina el número ---")

    numero_secreto = 7
    intentos = 0

    while True:
        try:
            intento = int(input("👉 Adivina el número del 1 al 10: "))
        except ValueError:
            print("⚠️ Ingresa un número entero válido.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("⬆️ ¡Muy bajo! El número es mayor.")
        elif intento > numero_secreto:
            print("⬇️ ¡Muy alto! El número es menor.")
        else:
            print(f"✅ ¡Correcto! Adivinaste en {intentos} intento(s).")
            break


if __name__ == "__main__":
    main()
