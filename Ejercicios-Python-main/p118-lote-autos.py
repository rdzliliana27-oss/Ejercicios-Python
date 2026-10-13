autos = [
    {"marca": "Ford", "modelo": "Mustang", "año": 1964},
    {"marca": "VW", "modelo": "Jetta", "año": 2015},
]

print("Lote de autos")
print("Agrega autos al inventario. Deja la marca vacia para terminar.")

while True:
    marca = input("Marca: ").strip()
    if not marca:
        break

    modelo = input("Modelo: ").strip()
    try:
        año = int(input("Año: "))
    except ValueError:
        print("Error: el año debe ser un numero entero.")
        continue

    autos.append({"marca": marca, "modelo": modelo, "año": año})

print(f"\nInventario completo: {len(autos)} autos")
print("-" * 45)
print(f"{'Marca':<15}{'Modelo':<18}{'Año':>8}")
print("-" * 45)
for auto in autos:
    print(f"{auto['marca']:<15}{auto['modelo']:<18}{auto['año']:>8}")

print("\nAutos en forma de registro:")
for auto in autos:
    for clave, valor in auto.items():
        print(f"{clave:<10}: {valor}")
    print()