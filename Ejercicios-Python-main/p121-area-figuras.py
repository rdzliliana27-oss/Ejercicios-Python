import math

figuras = {
    "Circulo": {"parametros": ["radio"], "formula": "pi * radio ** 2"},
    "Triangulo": {"parametros": ["base", "altura"], "formula": "base * altura / 2"},
    "Rectangulo": {"parametros": ["largo", "ancho"], "formula": "largo * ancho"},
}

print("Calculadora de areas")
print("Figuras disponibles:")
for nombre, datos in figuras.items():
    print(f"{nombre}: {datos['formula']}")

while True:
    figura = input("\nElige una figura: ").strip().title()
    if figura in figuras:
        break
    print("Figura no valida. Intenta de nuevo.")

medidas = {}
for parametro in figuras[figura]["parametros"]:
    try:
        medidas[parametro] = float(input(f"{parametro.title()}: "))
    except ValueError:
        print("Error: ingresa una medida numerica.")
        raise SystemExit

if figura == "Circulo":
    area = math.pi * medidas["radio"] ** 2
elif figura == "Triangulo":
    area = medidas["base"] * medidas["altura"] / 2
else:
    area = medidas["largo"] * medidas["ancho"]

print(f"Area del {figura}: {area:.4f}")