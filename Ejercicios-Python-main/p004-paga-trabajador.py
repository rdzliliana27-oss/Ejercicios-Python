# Programa para calcular la paga total de un trabajador
# usando un ciclo for para sumar cada día trabajado
# La paga debe ser mostrada con 2 decimales.


num_dias = int(input("Ingrese el número de días trabajados: "))
paga_diaria = float(input("Ingrese la paga por día: "))

total = 0.0

for dia in range(1, num_dias + 1):
    print(f"Día {dia}: paga = ${paga_diaria:.2f}")
    total += paga_diaria

print(f"\nLa paga total del trabajador es: ${total:.2f}")

