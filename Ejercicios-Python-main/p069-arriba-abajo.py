# ↕️ Imprime numeros de 1 a n o de n a 1 usando for.


def main():
    continuar = "S"
    while continuar == "S":
        print("\n↕️ 1. Contar de 1 a n")
        print("↕️ 2. Contar de n a 1")

        try:
            opcion = int(input("👉 Que eliges: "))
            limite = int(input("🎯 Cual es el limite: "))
            if limite < 1 or opcion not in (1, 2):
                raise ValueError
        except ValueError:
            print("⚠️ Error: opcion o limite no valido.")
            continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()
            continue

        if opcion == 1:
            secuencia = range(1, limite + 1)
        else:
            secuencia = range(limite, 0, -1)

        for numero in secuencia:
            print(numero, end=" ")
        print("\n✅ Conteo terminado.")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
