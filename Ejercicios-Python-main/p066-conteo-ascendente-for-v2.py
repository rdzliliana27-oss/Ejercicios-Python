# 🚀 Imprime los numeros de 1 a n en incrementos de m usando for.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                limite = int(input("🎯 Hasta donde contar: "))
                paso = int(input("📏 De cuanto en cuanto: "))
                if limite < 1 or paso < 1:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Error: introduce valores enteros positivos.")

        for numero in range(1, limite + 1, paso):
            print(numero, end=" ")
        print("\n✅ Conteo terminado.")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
