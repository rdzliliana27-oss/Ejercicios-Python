print("Lista de ciudades")

try:
    cantidad = int(input("Cuantas ciudades quieres registrar? "))
except ValueError:
    print("Error: ingresa una cantidad entera no negativa.")
else:
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
    else:
        ciudades = []
        for indice in range(cantidad):
            ciudad = input(f"Ciudad {indice + 1}: ").strip()
            if not ciudad:
                print("Error: el nombre de la ciudad no puede estar vacio.")
                break
            ciudades.append(ciudad)
        else:
            print(f"Ciudades registradas: {ciudades}")
            print(f"Ciudades en orden alfabetico: {sorted(ciudades, key=str.casefold)}")