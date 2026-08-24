# ejercicio 23: Verificar número
# Escribe un programa que solicite al usuario ingresar un número entero. El programa debe verificar
# si el número es positivo, negativo o cero, y mostrar un mensaje correspondiente en cada caso.


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