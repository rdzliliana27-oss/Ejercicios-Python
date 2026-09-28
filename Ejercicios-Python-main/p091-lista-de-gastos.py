# 🐾 Registro de gastos con listas y un gatito en la consola.

gastos = []

while True:
    print("\n" + "=" * 38)
    print("        🐱 MI LISTA DE GASTOS 🐱")
    print("          /\\_/\\")
    print("         ( o.o )")
    print("          > ^ <")
    print("=" * 38)
    print("1. Agregar un gasto")
    print("2. Ver todos los gastos")
    print("3. Eliminar un gasto")
    print("4. Ver el total")
    print("5. Salir")

    opcion = input("Elige una opcion (1-5): ")

    # 🐾 Cada gasto guarda su descripcion y su importe.
    if opcion == "1":
        descripcion = input("Descripcion del gasto: ").strip()
        if descripcion == "":
            print("La descripcion no puede quedar vacia.")
            continue

        while True:
            try:
                importe = float(input("Importe del gasto: $"))
            except ValueError:
                print("Escribe un importe numerico.")
                continue

            if importe <= 0:
                print("El importe debe ser mayor que cero.")
                continue
            break

        gastos.append([descripcion, importe])
        print(f"Listo, se agrego '{descripcion}' por ${importe:.2f}. 🐾")

    elif opcion == "2":
        if len(gastos) == 0:
            print("Todavia no hay gastos. El gatito espera tu primer registro. 🐱")
        else:
            print("\n--- GASTOS REGISTRADOS ---")
            for posicion, gasto in enumerate(gastos, start=1):
                print(f"{posicion}. {gasto[0]}: ${gasto[1]:.2f}")

    elif opcion == "3":
        if len(gastos) == 0:
            print("No hay gastos para eliminar. 🐱")
            continue

        print("\n--- GASTOS REGISTRADOS ---")
        for posicion, gasto in enumerate(gastos, start=1):
            print(f"{posicion}. {gasto[0]}: ${gasto[1]:.2f}")

        try:
            indice = int(input("Numero del gasto que quieres eliminar: "))
        except ValueError:
            print("Escribe un numero entero.")
            continue

        if 1 <= indice <= len(gastos):
            gasto_eliminado = gastos.pop(indice - 1)
            print(f"Se elimino '{gasto_eliminado[0]}'. 🐾")
        else:
            print("Ese numero no corresponde a un gasto.")

    elif opcion == "4":
        total = 0
        for gasto in gastos:
            total = total + gasto[1]
        print(f"Total de gastos: ${total:.2f}  (=^.^=)")

    elif opcion == "5":
        print("\nEl gatito se despide. ¡Hasta luego! 🐱")
        break

    else:
        print("Opcion no valida. Elige un numero del 1 al 5.")