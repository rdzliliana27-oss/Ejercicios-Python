##    p009-promedio-de-calificaciones.py
##    Calcula el promedio de varias calificaciones.
##    Las calificaciones se introducen separadas por coma.
## 


def leer_calificaciones(texto):
	"""Convierte una entrada como '8, 9.5, 10' en una lista de números."""
	calificaciones = []

	for pedazo in texto.split(","):
		pedazo = pedazo.strip()
		if pedazo == "":
			continue

		try:
			calificacion = float(pedazo)
		except ValueError:
			print(f"Se ignoró '{pedazo}' porque no es una calificación válida.")
			continue

		if 0 <= calificacion <= 10:
			calificaciones.append(calificacion)
		else:
			print(f"Se ignoró '{pedazo}' porque debe estar entre 0 y 10.")

	return calificaciones


def calcular_promedio(calificaciones):
	return sum(calificaciones) / len(calificaciones)


def main():
	print("===== PROMEDIO DE CALIFICACIONES =====")
	texto_entrada = input(
		"Escribe las calificaciones separadas por coma (ej: 8, 9.5, 10): "
	)

	calificaciones = leer_calificaciones(texto_entrada)

	if not calificaciones:
		print("No se ingresó ninguna calificación válida.")
		return

	promedio = calcular_promedio(calificaciones)
	print(f"Calificaciones válidas: {calificaciones}")
	print(f"Promedio: {promedio:.2f}")


if __name__ == "__main__":
	main()
