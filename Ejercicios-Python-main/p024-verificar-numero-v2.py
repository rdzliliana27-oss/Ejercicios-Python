def main():
    print("_________ VERIFICAR NUMERO V2 _________")

    numero = int(input("Ingrese un numero entero: "))

    if numero > 0:
        print("El numero es POSITIVO.")
    else:
        if numero < 0:
            print("El numero es NEGATIVO.")
        else:
            print("El numero es CERO.")

    print("Aqui terminamos de tomar decisiones.")


if __name__ == "__main__":
    main()