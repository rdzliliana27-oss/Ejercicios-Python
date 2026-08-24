def main():
    print("_________ CONVERTIR TEMPERATURAS _________")
    print("[C] Convertir Fahrenheit a Celsius")
    print("[F] Convertir Celsius a Fahrenheit")

    opcion = input("Elija una opcion: ").strip().upper()

    if opcion == "C":
        fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit:.2f} F equivalen a {celsius:.2f} C.")
    else:
        if opcion == "F":
            celsius = float(input("Ingrese los grados Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"{celsius:.2f} C equivalen a {fahrenheit:.2f} F.")
        else:
            print("Opcion no valida. Elija C o F.")


if __name__ == "__main__":
    main()