def main():
    print("_________ VERIFICAR NUMERO _________")

    numero = int(input("Ingrese un numero entero: "))

    if numero > 0:
        print("El numero es POSITIVO 👍.")
    if numero < 0:
        print("El numero es NEGATIVO 👎.")
    if numero == 0:
        print("El numero es CERO 😐.")

    print("Aqui terminamos de tomar decisiones.")


if __name__ == "__main__":
    main()