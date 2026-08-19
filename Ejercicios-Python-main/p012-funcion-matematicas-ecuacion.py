##    p012-funcion-matematicas-ecuacion.py
##    Evalúa una función matemática usando la biblioteca math.

import math as mt

def calcular_ecuacion(x, y):
	return 3 * mt.pow(x, 2) + mt.sqrt(mt.pow(x, 2) + mt.pow(y, 2)) + mt.exp(mt.log(x))

def main():
	print("===== FUNCIÓN MATEMÁTICA =====")
	print("Ecuación: f(x, y) = 3x² + √(x² + y²) + e^(ln(x))")
	x = float(input("Ingresa el valor de x (mayor que 0): "))
	y = float(input("Ingresa el valor de y: "))

	if x <= 0:
		print("El valor de x debe ser mayor que 0 para calcular ln(x).")
		return

	resultado = calcular_ecuacion(x, y)
	print(f"f({x}, {y}) = {resultado:.4f}")


if __name__ == "__main__":
	main()
