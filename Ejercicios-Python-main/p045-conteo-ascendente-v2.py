# 🔢 Ejercicio: conteo ascendente personalizado


def main():
    print("🔢 --- Conteo ascendente personalizado ---")

    try:
        inicio = int(input("👉 Ingresa el número inicial: "))
        fin = int(input("👉 Ingresa el número final: "))
    except ValueError:
        print("⚠️ Debes ingresar números enteros válidos.")
        return

    if inicio > fin:
        print("❌ El número inicial no puede ser mayor que el final.")
        return

    print("📈 Secuencia:")
    while inicio <= fin:
        print(f"➡️ {inicio}")
        inicio += 1


if __name__ == "__main__":
    main()
