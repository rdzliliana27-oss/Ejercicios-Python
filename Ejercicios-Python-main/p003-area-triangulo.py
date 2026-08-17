# Programa para calcular el área de un triángulo
# Fórmula: área = (base * altura) / 2


Base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

if Base <= 0 or altura <= 0:
    print("La base y la altura deben ser valores mayores que 0.")
else:
    area = (Base * altura) / 2
    print(f"El área del triángulo es: {area:.2f} unidades cuadradas")

