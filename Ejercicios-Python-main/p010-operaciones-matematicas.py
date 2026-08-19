##    p010-operaciones-matematicas.py
##    Calculadora de operaciones matemáticas.

def main():
	print("\n\n\n\n\n\n\n\n", end="")
	print('-' * 50)
	print('Calculadora de Operaciones Matemáticas')
	print('-' * 50)

	x = float(input("Ingresa el primer número: "))
	y = float(input("Ingresa el segundo número: "))

	suma = x + y
	resta = x - y
	multi = x * y
	divi = x / y
	modu = x % y
	pot = x ** y
	dive = x // y


	print ('Resultados de las operaciones matemáticas:')
	print(f'Suma : {suma:.2f}')
	print(f'Resta: {resta:.2f}')
	print(f'Mult : {multi:.2f}')
	print(f'Divi : {divi:.2f}')
	print(f'Modu : {modu:.2f}')
	print(f'Pot : {pot:.2f}')
	print(f'Dive : {dive:.2f}')


if __name__ == "__main__":
	main()
