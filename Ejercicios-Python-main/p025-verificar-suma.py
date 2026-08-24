## Ejercicio 25: Verificar suma de dos números
# Escribe un programa que solicite al usuario ingresar tres números enteros. El programa debe verificar si la suma de los dos primeros números es igual al tercer número. Si la suma es igual, el programa debe imprimir un mensaje indicando que la suma es correcta; de lo contrario, debe indicar que la suma es incorrecta.

def main():
    print("_________ VERIFICAR SUMA _________")

    numero_uno = int(input("Ingrese el primer numero: "))
    numero_dos = int(input("Ingrese el segundo numero: "))
    numero_tres = int(input("Ingrese el tercer numero: "))

    suma = numero_uno + numero_dos

    if suma == numero_tres:
        print(f"La suma de {numero_uno} + {numero_dos} es igual a {numero_tres}.")
    else:
        print(
            f"La suma de {numero_uno} + {numero_dos} es {suma}, "
            f"distinta de {numero_tres}."
        )


if __name__ == "__main__":
    main()