# Determina si un numero entero es un palindromo.


def main():
    continuar = "S"
    while continuar == "S":
        while True:
            try:
                numero = int(input("Introduce un numero para verificar si es palindromo: "))
                break
            except ValueError:
                print("Error: introduce un numero entero.")

        texto = str(numero)
        invertido = ""
        posicion = len(texto) - 1
        while posicion >= 0:
            invertido += texto[posicion]
            posicion -= 1

        if texto == invertido:
            print(f"El numero {numero} es un palindromo.")
        else:
            print(f"El numero {numero} no es un palindromo.")
        continuar = input("Desea continuar (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
