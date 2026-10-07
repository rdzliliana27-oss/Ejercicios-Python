try:
    limite = int(input("Calcular cuadrados de numeros pares hasta: "))
except ValueError:
    print("Error: ingresa un numero entero no negativo.")
else:
    if limite < 0:
        print("Error: el limite no puede ser negativo.")
    else:
        pares = [numero ** 2 for numero in range(1, limite + 1) if numero % 2 == 0]
        print(f"Cuadrados de los numeros pares hasta {limite}: {pares}")