##    p014-funciones-trigonometricas.py
##    Calcula funciones trigonométricas para un ángulo.

import math


def calcular_trigonometria(angulo: float) -> dict[str, float]:
	radianes = math.radians(angulo)
	return {
		"Seno": math.sin(radianes),
		"Coseno": math.cos(radianes),
		"Tangente": math.tan(radianes),
	}


def main():
	print("===== FUNCIONES TRIGONOMÉTRICAS =====")
	angulo = float(input("Ingresa un ángulo en grados: "))
	radianes = math.radians(angulo)

	print(f"Ángulo: {angulo:.2f} grados")
	print(f"Conversión: {radianes:.4f} radianes")

	for nombre, resultado in calcular_trigonometria(angulo).items():
		print(f"{nombre}: {resultado:.4f}")


if __name__ == "__main__":
	main()
