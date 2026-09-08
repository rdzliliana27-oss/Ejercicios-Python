# ✖️ Imprime, cuenta y suma los multiplos de m entre 1 y n.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                limite = int(input("🎯 Hasta donde: "))
                multiplo = int(input("✖️ Que multiplo quieres: "))
                if limite < 1 or multiplo == 0:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Error: limite positivo y multiplo distinto de cero.")

        multiplos = []
        for numero in range(1, limite + 1):
            if numero % multiplo == 0:
                multiplos.append(numero)

        print(f"✖️ Multiplos: {' '.join(map(str, multiplos))}")
        print(f"🔢 Cantidad: {len(multiplos)}")
        print(f"➕ Suma: {sum(multiplos)}")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
