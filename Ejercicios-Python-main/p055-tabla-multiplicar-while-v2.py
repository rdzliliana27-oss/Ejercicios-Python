# ✖️ Imprime las tablas desde la 1 hasta n, hasta el multiplo m.


def main():
    while True:
        while True:
            try:
                ultima_tabla = int(input("Hasta que tabla quieres? "))
                limite = int(input("Hasta donde la quieres? "))
            except ValueError:
                print("Error: introduce numeros enteros.")
                continue

            if ultima_tabla > 0 and limite > 0:
                break
            print("Error: los numeros deben ser mayores que 0.")

        tabla = 1
        while tabla <= ultima_tabla:
            contador = 1
            print(f"\n✖️ Tabla del {tabla}\n")
            while contador <= limite:
                print(f"{tabla} x {contador} = {tabla * contador}")
                contador += 1
            tabla += 1

        if input("\nDeseas continuar (S/N)? ").strip().upper() == "N":
            break

    print("\n✅ Gracias por utilizar este programa.")


if __name__ == "__main__":
    main()
