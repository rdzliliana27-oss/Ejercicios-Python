def main():
    print("===== CONVERSION DE CELSIUS A FAHRENHEIT =====")

    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f} grados")


if __name__ == "__main__":
    main()
