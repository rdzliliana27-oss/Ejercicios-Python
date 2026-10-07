import random

try:
    cantidad = int(input("Cuantos numeros aleatorios generar? "))
except ValueError:
    print("Error: ingresa una cantidad entera no negativa.")
else:
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
    else:
        numeros = [random.randint(1, 100) for _ in range(cantidad)]
        print(f"Numeros generados: {numeros}")
        print(f"Suma: {sum(numeros)}")