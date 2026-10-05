print("🐱 Filtro de números pares 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

cantidad = int(input("¿Cuántos números capturarás? "))
numeros = []

for posicion in range(cantidad):
    numeros.append(int(input(f"Número {posicion + 1}: ")))

pares = [numero for numero in numeros if numero % 2 == 0]

print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Cantidad de pares: {len(pares)}")