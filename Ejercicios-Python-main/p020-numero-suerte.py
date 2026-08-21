def main():
    print("===== NUMERO DE LA SUERTE =====")

    anio = input("Ingrese su anio de nacimiento de cuatro digitos: ").strip()

    if len(anio) != 4 or not anio.isdigit():
        print("Debe ingresar un anio con exactamente cuatro digitos.")
        return

    digitos = [int(digito) for digito in anio]
    suma = sum(digitos)

    print("Digitos:", *digitos, sep="\n")
    print(f"Suma de los digitos: {suma}")


if __name__ == "__main__":
    main()
