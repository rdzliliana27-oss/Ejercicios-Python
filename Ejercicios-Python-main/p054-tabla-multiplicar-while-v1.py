# ✖️ Imprime una tabla de multiplicar hasta el multiplo indicado.


def main():
    while True:
        while True:
            try:
                tabla = int(input("Que tabla quieres? "))
                limite = int(input("Hasta donde la quieres? "))
            except ValueError:
                print("Error: introduce numeros enteros.")
                continue

            if tabla > 0 and limite > 0:
                break
            print("Error: los numeros deben ser mayores que 0.")

        contador = 1
        print(f"\n✖️ Tabla del {tabla}")
        while contador <= limite:
            print(f"{tabla} x {contador} = {tabla * contador}")
            contador += 1

        if input("\nDeseas continuar (S/N)? ").strip().upper() == "N":
            break

    print("\n✅ Gracias por utilizar este programa.")


if __name__ == "__main__":
    main()
