# 🧮 Calcula la suma y el promedio de n numeros usando for.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                cantidad = int(input("🔢 Cuantos numeros deseas procesar: "))
                if cantidad < 1:
                    raise ValueError
                break
            except ValueError:
                print("⚠️ Error: introduce un entero positivo.")

        numeros = []
        for posicion in range(1, cantidad + 1):
            while True:
                try:
                    numero = float(input(f"🔢 Numero [{posicion}]: "))
                    break
                except ValueError:
                    print("⚠️ Error: introduce un numero.")
            numeros.append(numero)

        suma = sum(numeros)
        promedio = suma / cantidad
        print(f"📋 Numeros introducidos: {' '.join(map(str, numeros))}")
        print(f"➕ La suma es {suma:g} y el promedio es {promedio:g}.")
        continuar = input("🔁 Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
