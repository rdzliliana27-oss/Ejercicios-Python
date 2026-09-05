# Convierte a Fahrenheit cada temperatura Celsius de un rango.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                inicial = int(input("Introduce la temperatura inicial en C: "))
                final = int(input("Introduce la temperatura final en C: "))
            except ValueError:
                print("Error: introduce temperaturas enteras.")
                continue

            if inicial <= final:
                break
            print("Error: la temperatura inicial no puede ser mayor que la final.")

        print("-" * 20)
        temperatura = inicial
        while temperatura <= final:
            fahrenheit = temperatura * 9 / 5 + 32
            print(f"{temperatura} C = {fahrenheit:.1f} F")
            temperatura += 1

        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
