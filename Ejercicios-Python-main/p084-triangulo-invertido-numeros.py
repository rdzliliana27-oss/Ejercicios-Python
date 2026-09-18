# 🔢 Dibuja un triángulo numérico invertido.

numero = int(input("Dame un número: "))

for fila in range(numero, 0, -1):
    for valor in range(1, fila + 1):
        print(valor, end=" ")
    print()
