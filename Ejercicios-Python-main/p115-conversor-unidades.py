conversiones = {
    "longitud": {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000},
    "masa": {"g": 0.001, "kg": 1, "lb": 0.453592},
    "volumen": {"ml": 0.001, "l": 1, "gal": 3.78541},
}

print("Conversor de unidades")
print("Categorias disponibles:", ", ".join(conversiones))
categoria = input("Categoria: ").strip().lower()

if categoria not in conversiones:
    print("Error: categoria no reconocida.")
else:
    unidades = conversiones[categoria]
    print("Unidades disponibles:", ", ".join(unidades))
    origen = input("Convertir desde: ").strip().lower()
    destino = input("Convertir hacia: ").strip().lower()

    if origen not in unidades or destino not in unidades:
        print("Error: selecciona unidades de la categoria indicada.")
    else:
        try:
            cantidad = float(input(f"Cantidad en {origen}: "))
        except ValueError:
            print("Error: la cantidad debe ser numerica.")
        else:
            resultado = cantidad * unidades[origen] / unidades[destino]
            print(f"{cantidad:g} {origen} = {resultado:.6g} {destino}")