try:
    limite = int(input("Generar numeros impares hasta: "))
except ValueError:
    print("Error: ingresa un numero entero.")
else:
    if limite < 1:
        print("El limite debe ser mayor que cero.")
    else:
        impares = [numero for numero in range(1, limite + 1) if numero % 2 != 0]
        print(f"Numeros impares hasta {limite}: {impares}")