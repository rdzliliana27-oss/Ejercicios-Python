print("🐱 Clasificador de temperaturas 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

temperaturas = [8, 14, 18, 22, 27, 35]
clasificacion = [
    "Fría" if temperatura < 15 else
    "Templada" if temperatura <= 25 else
    "Caliente"
    for temperatura in temperaturas
]

print(f"Temperaturas: {temperaturas}")
print(f"Clasificación: {clasificacion}")