print("Multiplicacion de dos listas")

try:
    lista_a = [int(valor) for valor in input("Ingresa los numeros de la primera lista: ").split()]
    lista_b = [int(valor) for valor in input("Ingresa los numeros de la segunda lista: ").split()]
except ValueError:
    print("Error: ingresa solamente numeros enteros.")
else:
    if len(lista_a) != len(lista_b):
        print("Error: ambas listas deben tener la misma cantidad de elementos.")
    else:
        productos = [a * b for a, b in zip(lista_a, lista_b)]
        print(f"Primera lista: {lista_a}")
        print(f"Segunda lista: {lista_b}")
        print(f"Producto elemento a elemento: {productos}")