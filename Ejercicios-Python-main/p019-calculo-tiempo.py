def main():
    print("===== CONVERSION DE TIEMPO =====")

    horas = int(input("Ingrese la cantidad de horas: "))

    dias = horas / 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"Dias: {dias:.2f}")
    print(f"Minutos: {minutos}")
    print(f"Segundos: {segundos}")


if __name__ == "__main__":
    main()
