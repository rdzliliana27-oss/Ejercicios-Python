# 💱 Tabla de conversion de pesos a dolares.


def main():
    tipo_cambio = 20.71

    while True:
        print("\n💱 Tabla de conversion de pesos a dolares")
        print(f"Tipo de cambio: {tipo_cambio:.2f} pesos por dolar")
        print("-" * 32)

        while True:
            try:
                valor_inicial = float(input("Valor inicial: "))
                valor_final = float(input("Valor final: "))
            except ValueError:
                print("Error: introduce valores numericos.")
                continue

            if valor_inicial > 0 and valor_final > valor_inicial:
                break
            print("Error: el valor final debe ser mayor que el inicial y ambos positivos.")

        valor = valor_inicial
        print("\n📊 Pesos\tDolares")
        print("-" * 22)
        while valor <= valor_final:
            print(f"{valor:.2f}\t{valor / tipo_cambio:.2f}")
            valor += 1

        if input("\nDeseas continuar (S/N)? ").strip().upper() == "N":
            break


if __name__ == "__main__":
    main()
