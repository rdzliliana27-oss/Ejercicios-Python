# 💥 Imprime los numeros de n a 1 en decrementos de m usando for.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                inicio = int(input("🎯 Desde donde contar: "))
                paso = int(input("📏 De cuanto en cuanto: "))
                if inicio < 1 or paso < 1:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Error: introduce valores enteros positivos.")

        for numero in range(inicio, 0, -paso):
            print(numero, end=" ")
        print("\n✅ Cuenta terminada.")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
