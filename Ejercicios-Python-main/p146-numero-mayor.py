# p146-numero-mayor.py
# Dados tres números enteros, regresa el mayor


def numero_mayor(n1: int, n2: int, n3: int) -> int:
    mayor = n1
    if n2 > mayor:
        mayor = n2
    if n3 > mayor:
        mayor = n3
    return mayor


print("Dame tres numeros enteros separados por enter:")
a = int(input())
b = int(input())
c = int(input())
print(f"El número mayor es: {numero_mayor(a, b, c)}")
