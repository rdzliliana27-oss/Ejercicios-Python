tasas_en_mxn = {
    "MXN": 1.0,
    "USD": 17.2,
    "EUR": 18.6,
    "CAD": 12.5,
}

print("Conversor de divisas (tasas de ejemplo en pesos mexicanos)")
print("Divisas disponibles:", ", ".join(tasas_en_mxn))
origen = input("Divisa de origen: ").strip().upper()
destino = input("Divisa de destino: ").strip().upper()

if origen not in tasas_en_mxn or destino not in tasas_en_mxn:
    print("Error: selecciona una de las divisas disponibles.")
else:
    try:
        cantidad = float(input(f"Cantidad en {origen}: "))
    except ValueError:
        print("Error: la cantidad debe ser numerica.")
    else:
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativa.")
        else:
            cantidad_mxn = cantidad * tasas_en_mxn[origen]
            resultado = cantidad_mxn / tasas_en_mxn[destino]
            print(f"{cantidad:.2f} {origen} = {resultado:.2f} {destino}")