import math

def area_circulo(radio):
    return math.pi * radio ** 2


radio = float(input("Ingresa el radio del circulo: "))

if radio <= 0:
    print("El radio debe ser mayor que 0.")
else:
    area = area_circulo(radio)
    print(f"El area del circulo es: {area:.2f} unidades cuadradas")