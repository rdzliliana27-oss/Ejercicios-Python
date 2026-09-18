# 🏦 Simula un plan de ahorro con depósitos mensuales.

saldo = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
tasa = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

print("\n--- Plan de Ahorro Detallado ---")

for mes in range(1, meses + 1):
    saldo_inicial = saldo
    interes = saldo_inicial * tasa / 100
    saldo = saldo_inicial + interes + deposito
    print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo:.2f}")

print(f"\nAl final de {meses} meses, tendrás ${saldo:.2f}")
