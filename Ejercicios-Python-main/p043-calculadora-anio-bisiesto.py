#Ejericio de año bisiesto

def main():
    print("📆 --- Calculadora de año bisiesto ---")
    anio = int(input("Año: "))

    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        print(f"✅ El año {anio} es bisiesto.")
    else:
        print(f"❌ El año {anio} no es bisiesto.")


if __name__ == "__main__":
    main()