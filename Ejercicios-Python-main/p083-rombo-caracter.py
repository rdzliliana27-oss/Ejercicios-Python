# ♦️ Dibuja un rombo con un número impar de filas.

altura = int(input("Dame un número impar para la altura: "))
caracter = input("¿Qué carácter quieres usar? ")

mitad = altura // 2 + 1

for fila in range(1, altura + 1):
    if fila <= mitad:
        cantidad = 2 * fila - 1
        espacios = mitad - fila
    else:
        cantidad = 2 * (altura - fila) + 1
        espacios = fila - mitad
    print(" " * espacios + caracter * cantidad)
