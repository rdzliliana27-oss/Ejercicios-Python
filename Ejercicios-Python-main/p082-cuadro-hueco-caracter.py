# ⬜ Dibuja el contorno de un cuadrado.

lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

for fila in range(1, lado + 1):
    for columna in range(1, lado + 1):
        if fila == 1 or fila == lado or columna == 1 or columna == lado:
            print(caracter, end=" ")
        else:
            print(" ", end=" ")
    print()
