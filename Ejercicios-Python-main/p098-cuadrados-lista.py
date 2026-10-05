print("🐱 Cuadrados de números 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

n = int(input("¿Hasta qué número? "))
numeros = list(range(1, n + 1))
cuadrados = [numero ** 2 for numero in numeros]

print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")