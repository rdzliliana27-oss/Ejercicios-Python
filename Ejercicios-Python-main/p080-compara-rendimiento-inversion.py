# 💰 Compara el crecimiento de dos fondos de inversión.

monto_a = float(input("--- Fondo de Inversión A ---\nMonto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

monto_b = float(input("\n--- Fondo de Inversión B ---\nMonto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

años = int(input("\nAños a proyectar: "))

saldo_a = monto_a
saldo_b = monto_b

print("\n--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A | Fondo B")
print("-------------------------------------------")

for año in range(1, años + 1):
    saldo_a = saldo_a + saldo_a * tasa_a / 100
    saldo_b = saldo_b + saldo_b * tasa_b / 100
    print(f"{año} | ${saldo_a:.2f} | ${saldo_b:.2f}")

if saldo_a > saldo_b:
    print(f"Resultado final: El Fondo A (${saldo_a:.2f}) superó al Fondo B (${saldo_b:.2f}).")
elif saldo_b > saldo_a:
    print(f"Resultado final: El Fondo B (${saldo_b:.2f}) superó al Fondo A (${saldo_a:.2f}).")
else:
    print(f"Resultado final: Los dos fondos terminaron con ${saldo_a:.2f}.")
