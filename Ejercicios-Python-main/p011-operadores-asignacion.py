##    p011-operadores-asignacion.py
##    Ejemplo sencillo de operadores de asignación.


def main():
	print("===== OPERADORES DE ASIGNACIÓN =====")
	x = float(input("Ingresa un número: "))
	
	resultado = x
	
	print(f"x = {resultado}")

	resultado = x
	resultado += 3
	print(f"x += 3   -> {resultado}")

	resultado = x
	resultado -= 3
	print(f"x -= 3   -> {resultado}")

	resultado = x
	resultado /= 3
	print(f"x /= 3   -> {resultado}")

	resultado = x
	resultado %= 3
	print(f"x %= 3   -> {resultado}")

	resultado = x
	resultado **= 3
	print(f"x **= 3  -> {resultado}")

	resultado = x
	resultado //= 3
	print(f"x //= 3  -> {resultado}")


if __name__ == "__main__":
	main()


