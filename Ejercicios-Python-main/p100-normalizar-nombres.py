print("🐱 Normalizador de nombres 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

nombres = [" ana", "LUIS ", "", " maría josé ", "Pedro"]
normalizados = [
    nombre.strip().title()
    for nombre in nombres
    if nombre.strip()
]

print(f"Datos originales: {nombres}")
print(f"Nombres normalizados: {normalizados}")