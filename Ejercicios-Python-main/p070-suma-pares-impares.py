# ➕ Muestra y suma los numeros pares e impares de 1 a n.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                limite = int(input("🎯 Dame el valor final: "))
                if limite < 1:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Error: introduce un entero positivo.")

        pares = []
        impares = []
        for numero in range(1, limite + 1):
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)

        print(f"🔵 Pares: {' '.join(map(str, pares))}")
        print(f"➕ Suma de pares: {sum(pares)}")
        print(f"🟠 Impares: {' '.join(map(str, impares))}")
        print(f"➕ Suma de impares: {sum(impares)}")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
