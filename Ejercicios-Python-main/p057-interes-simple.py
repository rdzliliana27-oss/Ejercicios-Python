# 💰 Calcula los anos necesarios para alcanzar una meta con interes simple.


def main():
    while True:
        while True:
            try:
                capital_inicial = float(input("Introduce el capital inicial: "))
                tasa_interes = float(input("Introduce la tasa de interes anual (%): "))
                meta_ahorro = float(input("Introduce la meta de ahorro: "))
            except ValueError:
                print("Error: introduce valores numericos.")
                continue

            if capital_inicial > 0 and tasa_interes > 0 and meta_ahorro > capital_inicial:
                break
            print("Error: los valores deben ser positivos y la meta mayor que el capital inicial.")

        capital_actual = capital_inicial
        interes_anual = capital_inicial * tasa_interes / 100
        anos = 0

        while capital_actual < meta_ahorro:
            capital_actual += interes_anual
            anos += 1

        print("\n💰 Resultado del ahorro")
        print("-" * 50)
        print(f"Para alcanzar la meta de ${meta_ahorro:,.2f}, necesitaras {anos} anos.")
        print(f"El monto final acumulado sera de ${capital_actual:,.2f}.")
        print("-" * 50)

        if input("\nDeseas realizar otro calculo (S/N)? ").strip().upper() == "N":
            break

    print("\n✅ Fin del programa.")


if __name__ == "__main__":
    main()
