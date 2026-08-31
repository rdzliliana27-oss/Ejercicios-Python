# 🔽 Ejercicio: conteo descendente personalizado


def main():
    print("🔽 --- Conteo descendente personalizado ---")

    try:
        inicio = int(input("👉 Ingresa el número inicial: "))
        fin = int(input("👉 Ingresa el número final: "))
    except ValueError:
        print("⚠️ Debes ingresar números enteros válidos.")
        return

    if inicio < fin:
        print("❌ El número inicial no puede ser menor que el final.")
        return

    print("📉 Secuencia:")
    while inicio >= fin:
        print(f"⬅️ {inicio}")
        inicio -= 1


if __name__ == "__main__":
    main()
